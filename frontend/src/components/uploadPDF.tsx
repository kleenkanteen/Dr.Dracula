import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
 
export function UploadPDF() {
  return (
    <div className="grid w-full max-w-sm items-center gap-1.5">
      <Label htmlFor="blood-pdf">Upload PDF of blood test</Label>
      <Input id="blood-pdf" type="file" />
    </div>
  )
}