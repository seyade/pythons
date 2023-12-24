from openai import OpenAI

client = OpenAI()

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system", 
      "content": "You are Lead Software Engineer with over 10 years experience in the field. You are an expert in React, Typescript, JavaScript, Next.js, Express, Node.js, SQL, GraphQL, Python, OpenAI, AWS Lambda, Java, C#, HTML and CSS. You also know AWS and CI/CD devops using GitHub Actions, Docker and Kubernetes, so this means that you know how to deploy and manage apps to production and other environments. All these make you a good Software Architect that enable you to come up with excellent software architecture. So you are good in Frontend and Backend engineering"
    },
    {
      "role": "user", 
      "content": "I have an idea of a SaaS platform that helps onboarding new developers into a team and project. The idea is to help new developers to learn and get acustomed to the project, its architecture on the frontend and the backend, and how they interact with each other. This will not only save time but also reduce frustrations that many new developers face when they get introduced to a project. The platform has also access to the repository of the project on Github, which is also cloned in the SaaS platform itself to show where the files and folders are. Now I want you to tell me what would you make the SaaS platform do to facilitate the onboarding to make the life of the new developer easy, when learning about the project? UX wise and tech wise."
    }
  ]
)

print(completion.choices[0].message)
