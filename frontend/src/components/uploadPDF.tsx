"use client";
import { useTheme } from "next-themes";
import { useState } from "react"
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
import markdownit from 'markdown-it';


// commenting out because of a type error on FileList. due to nextjs 14 issue. 
// the server does not have access to FileList, which is a browser API. idk why when this file is client compoennt
// mdn docs https://developer.mozilla.org/en-US/docs/Web/API/FileList
// someone had the same issue: https://github.com/orgs/react-hook-form/discussions/11096
const formSchema = z.object({
  file: z.any().optional(),
});

export function UploadPDF() {
  const [bloodReport, setBloodReport] = useState("");
  const { setTheme } = useTheme()
  setTheme("dark");

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
  });

  const fileRef = form.register("file");

  const onSubmit = async (data: any) => {
    try {
      const apiURL = process.env.NEXT_PUBLIC_API_URL ? process.env.NEXT_PUBLIC_API_URL : "http://localhost:8000/blood-test";
      const url = new URL(apiURL);
      const formData = new FormData();
      formData.append("upload_file", data.file[0]);

      const fetchOptions = {
        method: "POST",
        body: formData,
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Request-Headers": "*",
          "Access-Control-Request-Method": "*"
        },
      };
      
      setBloodReport("Analyzing data...");
      
      let result = await fetch(url, fetchOptions);
      console.log("uploaded file:", data.file[0].name);

      // clear file input
      let fileInput = (document.getElementById("blood-pdf") as HTMLInputElement);
      fileInput.value = "";

      let json_res = await result.json();
      const md = markdownit()
      const md_res = md.render(json_res["report"]);

      setBloodReport(md_res);
    } catch(error){
      console.error("failed to upload file: " + error);
    }
  };

  return (
    <>
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
      {bloodReport ? (
        <Card className="w-full results-card">
          <CardHeader>
            <CardTitle>Report</CardTitle>
            <CardDescription>Report Analysis of biomarker data</CardDescription>
          </CardHeader>
          <CardContent>
            <div dangerouslySetInnerHTML={{ __html: bloodReport }} />
          </CardContent>
        </Card>
      ): null}
      
    </>
    
  )
}