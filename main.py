import sys
import glob
from os import path
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import TextLoader

rules = """
1. The Readme should have a title and a description describing the purpose of the project (score=3)
2. The Readme should have a section for table of contents (score=1)
3. The Readme should have instructions on how to get started and run the project (score=3)
4. The Readme should have instructions on how to run tests (score=2)
5. The Readme should have a section containing prerequisites such as knowledge needed, OS requirements, etc (score=1)
6. The Readme should contain contributing guidelines (score=2)
"""

def load_readme(directory_location, filename="README.md"):
    readme_path = path.join(directory_location, filename)
    f = open(readme_path)
    return f.readlines()

def validate_readme(directory_location):

    readme_contents = load_readme(directory_location)
    exemplar = load_readme("./sample", "exemplar-README.md")

    validate_prompt = """Your task is to validate the contents of the Readme file based on the following rules

    {rules}

    Please use the following markdown as an exemplar Readme example:

    ```md
    {exemplar}
     ```

    Now, could you evaluate the following Readme:

    ```md
    {readme}
    ```

    Could you please respond with the score for the Readme based on the scores mentioned next to each rule?
    Please also list out which rules passed and which ones failed also providing rule description in a table. 
    """

    prompt = PromptTemplate(template=validate_prompt, input_variables=["readme", "rules", "exemplar"])
    llm = OpenAI(temperature=0)
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    return llm_chain.run(readme=readme_contents, rules=rules, exemplar=exemplar)

def generate_readme(directory_location):

    exemplar = load_readme("./sample", "exemplar-README.md")
    generate_prompt = """Your task is to generate a Readme based on the following rules:

    {rules}

    Please use the following markdown as an exemplar Readme example:

    ```md
    {exemplar}
     ```

     Please use the files here to generate the readme.

    """
    
    prompt = PromptTemplate(template=generate_prompt, input_variables=["rules", "exemplar"])
    llm = OpenAI(model="text-davinci-003", temperature=0)
    chain = load_qa_chain(chain_type="refine", llm=llm, verbose=True)

    documents = []

    for filename in glob.iglob(directory_location + '**/**', recursive=True):
        if not(path.isdir(filename)) and not("README" in filename) and not("go.sum" in filename):
            loader = TextLoader(filename)
            docs = loader.load()
            documents.append(docs[0])

    return chain.run(input_documents=documents, question=prompt.format(rules=rules, exemplar=exemplar))

if __name__ == '__main__':
    directory_location = sys.argv[1]
    print(validate_readme(directory_location))
    # print(generate_readme(directory_location))
