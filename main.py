import openai
from dotenv import find_dotenv, load_dotenv
#load the environment variables-setup the OpenAI API client 
load_dotenv()

client = openai.OpenAI()
model = "gpt-3.5-turbo"
#create our asistant id
personal_trainer_assis =client.beta.assistants.create(
    name="Personal Trainer",
    instructions="""You are the best trainer""",
    model=model
)
assistant_id=personal_trainer_assis.id
print(assistant_id)


"""#creat thread id"""
thread = client.beta.threads.create(
    messages=[
        {
            "role":"user",
            "content":"How do I get started to reduce my tummy"
        }
    ]
 
)
thread_id = thread.id
print(thread_id)

""" #create a message
message ="what are the best excercise to reduce tummy and lean muscles"
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content=message
)
#run our Assistant
run=client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id,
    instructions="Please address the user as Maniba"
)
def wait_for_run_completion(client, thread_id, run_id, sleep_interval=5):
    """
    Waits for a run to complete and prints the elapsed time.:param
    :param thread_id: the id of thread
    :param run_id: the id of run
    :param sleep_interval: time in seconds to wait between checks.
    """
    while True:
        try:
            run = client.beta.threads.runs.retrieve(thread_id=thread_id)
            if run.completed_at:
                elapsed_time = run.completed_at - run.created_at
                formatted_elapsed_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time)
                )
                print(f"Run completed in {formatted_elapsed_time}")
                logging.info(f"Run completed in {formatted_elapsed_time}")
                #get message here once Run is completed
                messages= client.beta.threads.messages.list(thread_id=thread_id)
                last_message= messages.data[0]
                response = last_message.content[0].text.value
                print(f"Assistance Response: {response}")
                break
        except Exception as e:
            logging.error(f"An error ocurred while retrieving the run:{e} ")
            break
logging.info("Waiting for run to complete...")
time.sleep(sleep_interval)
#run
wait_for_run_completion(client=client,thread_id=thread_id,run_id=run.id) """