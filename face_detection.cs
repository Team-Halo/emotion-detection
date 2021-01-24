using System;
using System.IO;
using System.Diagnostics;

class Example
{
    public static void Main()
    {
        using (Process process = new Process())
        {
            process.StartInfo.FileName = "emotion.py";
            process.StartInfo.UseShellExecute = false;
            process.StartInfo.RedirectStandardOutput = true;
            process.StartInfo.RedirectStandardInput = true;
            process.Start();

            StreamReader reader = process.StandardOutput;
            StreamWriter writer = process.StandardInput;

            while (true) 
            {
                // Synchronously read the standard output of the spawned process.
                string output = reader.ReadToEnd();

                if (output == "frowning") 
                {
                    // Frowning procedure
                }
                else if (output == "sleeping")
                {
                    // Sleeping procedure
                }
                else if (output == "happy")
                {
                    // Happy procedure
                }

                // To pause the face detection:
                // writer.WriteLine("p");
                
                // To resume the face detection:
                // writer.WriteLine("r");

                // To quit the face detection:
                // writer.WRiteLine("q");
            }
            
            process.WaitForExit();
        }
    }
}