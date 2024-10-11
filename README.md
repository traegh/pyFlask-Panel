This project presents a simple web interface with a dark theme that can serve as a frontend for a manual chatbot. The project is built using Flask and JavaScript, with a view to later integration with Playwright-based automation.

## Features

- Interface with a dark theme
- Checkbox with 5 test options
- Text field for entering messages (max 500 characters)
- Button for sending messages
- Enter key support for sending messages
- Custom Tab key support for random selection of options

## Requirements

- Python 3.6+
- Flask

## Installation

1 Clone the repository:
   ```
   git clone https://github.com/traegh/pyFlask-Panel.git
   cd pyFlask-Panel
   ```

2 Install the required dependencies:
   ```
   pip install flask
   ```

## Launching the application

1 Start the Flask server:
   ```
   python app.py
   ```

2. open a browser and go to `http://localhost:5000`.

## Project structure

```
/project
    /templates
        index.html
    app.py
    README.md
```

## Usage

- Select an option from the drop-down list
- Type the message in the text field
- Send the message by clicking the “Send” button or pressing Enter
- Use the Tab key to randomly select an option from the drop-down list

## Further development

- Adding real chatbot functionality
- Implementation of data persistence
- Extending the interface with more features

## License

MIT License.

## Contact

Discord: Elusive1337

Translated with DeepL.com (free version)
