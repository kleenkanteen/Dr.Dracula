"use client";
import { useTheme } from "next-themes";

import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle
} from "@/components/ui/card";
import {
  Form,
  FormControl,
  FormField,
  FormItem, FormMessage
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";

// commenting out because of a type error on FileList. due to nextjs 14 issue. 
// the server does not have access to FileList, which is a browser API. idk why when this file is client compoennt
// mdn docs https://developer.mozilla.org/en-US/docs/Web/API/FileList
// someone had the same issue: https://github.com/orgs/react-hook-form/discussions/11096
const formSchema = z.object({
  file: z.any().optional(),
});

export function UploadPDF() {
  const { setTheme } = useTheme()

  setTheme("dark");

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
  });

  const fileRef = form.register("file");

  const onSubmit = (data: any) => {
    try {
      const url = new URL("http://localhost:8000/blood-test");
      const formData = new FormData();
      formData.append("file", data.file[0]);

      const fetchOptions = {
        method: "POST",
        body: formData,
      };

      fetch(url, fetchOptions);
      console.log("uploaded file:", data.file[0].name);
    }
    catch {
      console.log("failed to upload file");
    }
  };

  return (
    <Card className="lg:max-w-md w-full upload-blood-card">
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="w-full p-10">
          <CardHeader>
            <CardTitle>Upload PDF</CardTitle>
            <CardDescription>Upload your blood test results</CardDescription>
          </CardHeader>
          <CardContent>
            <FormField
              control={form.control}
              name="file"
              render={({ field }) => {
                return (
                  <FormItem>
                    <FormControl>
                      <Input id="blood-pdf" type="file" {...fileRef} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                );
              }}
            />
          </CardContent>
          <CardFooter>
            <Button type="submit">Upload</Button>
          </CardFooter>
        </form>
      </Form>
    </Card>
  )
}