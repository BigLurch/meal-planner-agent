from langchain.agents import create_agent

from util.models import get_model
from util.streaming_utils import STREAM_MODES, handle_stream
from util.pretty_print import get_user_input
from meal_planner_prompt import SYSTEM_PROMPT

def run():
    # Get predefined attributes
    model = get_model()

    # Create agent
    agent = create_agent(
        model=model,
        system_prompt=SYSTEM_PROMPT,
    )

    messages = []

    while True:
        user_input = get_user_input(
            "Vad vill du ha hjälp med i din matplan? (skriv 'exit', 'quit', 'avsluta' eller 'q' för att avsluta)"
        )

        if user_input.lower() in ["exit", "quit", "avsluta", "q"]:
            print("Avslutar programmet.")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            process_stream = agent.stream(
                {"messages": messages},
                stream_mode=STREAM_MODES,
            )

            assistant_text = handle_stream(
                process_stream,
                agent_name="Meal Planner Agent",
            )

            messages.append({"role": "assistant", "content": assistant_text})

        except Exception as e:
            print(f"Ett fel uppstod: {e}")


if __name__ == "__main__":
    run()