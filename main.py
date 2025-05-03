import argparse
from extract import extract_text_from_pptx
from vector_db import init_collection, add_documents, query_documents
from rag import build_prompt, run_chat
# from config import SLIDE_PATH, SKIP_SLIDES

def main():
    parser = argparse.ArgumentParser(description="Ask questions on PowerPoint slides using RAG")

    parser.add_argument("file", help="Path to the .pptx file")
    parser.add_argument("question", help="The question to ask about the slides")
    parser.add_argument("--skip", type=int, default=0, help="Number of initial slides to skip")
    parser.add_argument("--top_k", type=int, default=2, help="Number of top results to retrieve")

    args = parser.parse_args()

    docs = extract_text_from_pptx(args.file)
    collection = init_collection()
    add_documents(collection, docs, start_slide=args.skip + 1)

    results = query_documents(collection, args.question)
    # print(results)
    documents = results['documents'][0]
    slide_num = results['metadatas'][0][0]['slide']

    if not documents:
        print("No relevant content found.")
        return

    prompt = build_prompt(args.question, documents)
    stream = run_chat(prompt)

    print("\n--- Response ---\n")
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
    print(f"\n ** Content drawn from slide No. {slide_num} ** \n")

if __name__ == "__main__":
    main()
