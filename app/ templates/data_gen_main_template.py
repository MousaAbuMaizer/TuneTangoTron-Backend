data_gen_main_template = """
 *ROLE*
<YOU ARE A PROFESSIONAL PROMPT GENERATOR ASSISTANT THAT GENERATE PROMPTS FOR lARGE LANGUAGE MODELS BASED ON A CERTAIN TOPIC {topic}>

                    *TASK*
<Your task is to generate a series of structured dialogue data. The dialogue should simulate interactions between a user and an AI assistant regarding the specified topic. The assistant's role is to provide helpful responses and guidance to the user's inquiries or statements based on the topic given.>

                   *OUTPUT FORMAT*
< the generated data should be Structured as below:>
  1."SystemMessage": "you are a useful AI assistant",
  2. "HumanMessage": "",
  3. "AssistantMessage": ""


                     *RULES*
1. The 'SystemMessage' should be assisting the user on the provided topic
2. The 'HumanMessage' must be questions or inquries related to the topic only
3. The 'AssistantMessage' should be consise and clear answers to the HumanMessage
4. The 'AssistantMessage' must always stay  relevant to the topic


                    *OUTPUT RULES*
<Generate only five responses or examples>


                    *EXAMPLE*
 <the topic was about cars the output should be:>
                    
  "SystemMessage": "You are a useful AI assistant.",
  "HumanMessage": "How does hybrid car technology work?",
  "AssistantMessage": "Hybrid car technology combines an internal combustion engine with an electric motor and battery. The engine charges the battery, which then powers the electric motor. This setup allows hybrids to achieve better fuel efficiency and lower emissions compared to traditional vehicles."


  "SystemMessage": "You are a useful AI assistant.",
  "HumanMessage": "What are the benefits of hydrogen fuel cell vehicles?",
  "AssistantMessage": "Hydrogen fuel cell vehicles offer several benefits, including zero emissions, longer driving ranges compared to electric vehicles, and faster refueling times. They also provide a more sustainable alternative to conventional gasoline-powered cars."


  "SystemMessage": "You are a useful AI assistant.",
  "HumanMessage": "Can you explain the concept of regenerative braking in electric cars?",
  "AssistantMessage": "Regenerative braking in electric cars captures kinetic energy during braking and converts it into electrical energy, which is then stored in the battery. This process helps improve the overall efficiency of electric vehicles by extending their range and reducing energy waste."



"""