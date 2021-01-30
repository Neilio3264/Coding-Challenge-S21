# ACM Research Coding Challenge (Spring 2021)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge-S21`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Submit your solution by filling out this [form](https://acmutd.typeform.com/to/uqAJNXUe).

## Question One

Genome analysis is the identification of genomic features such as gene expression or DNA sequences in an individual's genetic makeup. A genbank file (.gb) format contains information about an individual's DNA sequence. The following dataset in `Genome.gb` contains a complete genome sequence of Tomato Curly Stunt Virus.

**With this file, create a circular genome map and output it as a JPG/PNG/JPEG format.** We're not looking for any complex maps, just be sure to highlight the features and their labels.

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

## Answer One

The creation of the circular genome map was made using python. In specific, `python3.8.5`.

The following python libraries and their use are as follows:

1. `Biopython` : This is a tool for computational molecular biology. This library was the core library used to parse the genbank and create the diagram.

   Can be installed with python3.6/3.7/3.8

   `pip install biopython` or `python -m pip install biopython`

2. `ReportLab` : This is a tool for producing pdf reports for python data. Using the included `pillow` library, ReportLab can also produce bitmap images.

   `pip install reportlab` or `python -m pip install reportlab`

The solution for creating the circular genome map was created using these two libraries. First, I did research to find these libraries which proved to be the easiest to implement. After setting them up, I first understood the data output and how to parse it shown in `parse.py`. After understanding the data, I created a variable to hold the data. Then, setup an empty diagram to then add to. The features within the record were then looped through only accepting the ones of type gene. Alternating colors where then applied to each feature with a label at the end of them to make for easier reading. This feature would be added a feature set. The features where finally drawn into the diagram and two images were created (One PNG and one JPG).
