LightWeight CLI for RAG on PowerPoint Presentations. Minimal Dependencies. Completely built on Open-Source stack including Ollama for LLMs. 

## Installation

1. Clone the repo
2. Install dependencies
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
3. Ensure that Ollama is downloaded and a model is pulled. (Go to ollama.com for instructions on how to set up)
4. Usage
   
   Run the CLI
   ```bash
   python main.py path/to/your_slide.pptx "Your question here"
   ```
   Optional Args:
   --skip: Skip initial N slides (default: 3)  This is to skip the slide Title, Table of Contents etc:-
   --top_k: Number of results to retrieve (default: 2)

5. If everything goes right you will get a response from the LLM based on your slide and also a reference to the Slide Number from which the context was drawn. (Super Useful if you're working with a really large ppt :))

This Project uses gemma2:2b as the LLM and chromadb as the vector store by default. 

## Contributing

Pull requests are welcome. Please fork the repo and submit a PR!

## License

MIT License. See LICENSE file for details.
