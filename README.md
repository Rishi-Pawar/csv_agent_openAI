# csv_agent_openAI

# CSV Agent for Titanic Dataset

## Description
This Streamlit app allows users to interact with the Titanic dataset using natural language queries powered by LangChain's CSV Agent and OpenAI's `gpt-3.5-turbo`. Users can input questions about the dataset, and the app processes them to provide accurate responses or analyses.

### Features
- Interactive Q&A interface for the Titanic dataset.
- Powered by OpenAI's `gpt-3.5-turbo` for advanced query handling.
- Built using LangChain's experimental CSV Agent for seamless data analysis.

---

## Dataset
The app requires the Titanic dataset (`titanic.csv`) with the following columns:
- `PassengerId`: Unique identifier for passengers.
- `Survived`: Survival status (0 = Dead, 1 = Alive).
- `Pclass`: Passenger class (1 = First Class, 2 = Second Class, 3 = Third Class).
- `Name`: Passenger's name.
- `Sex`: Gender (male, female).
- `Age`: Passenger's age.
- `SibSp`: Number of siblings/spouses aboard.
- `Parch`: Number of parents/children aboard.
- `Ticket`: Ticket number.
- `Fare`: Ticket fare.

---

## How to Run
### Prerequisites
1. Install Python (3.8 or later).
2. Obtain an OpenAI API key from the [OpenAI website](https://platform.openai.com/).

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
