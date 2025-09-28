# MBA Software Engineering with AI Challenge - Full Cycle

## 📋 About the Project

This project implements a **RAG (Retrieval-Augmented Generation)** system that allows asking questions about PDF documents using artificial intelligence. The system uses:

- **PostgreSQL with pgvector** for vector embeddings storage
- **OpenAI** for embeddings generation and responses
- **LangChain** for RAG pipeline orchestration
- **Docker** for service containerization

### 🏗️ Architecture

```
PDF Document → Ingestion → Vector Store (PostgreSQL) → Search → Chat Interface
```

1. **Ingestion**: The PDF document is processed, split into chunks and converted to embeddings
2. **Storage**: Embeddings are stored in PostgreSQL with pgvector extension
3. **Search**: When a question is asked, the system searches for the most relevant chunks
4. **Generation**: The LLM generates a response based on the found context

## 🚀 Prerequisites

- **Docker** and **Docker Compose**
- **Python 3.9+**
- **OpenAI account** with valid API key

## ⚙️ Configuration

### 1. Clone the repository

```bash
git clone <repository-url>
cd mba-ia-desafio-ingestao-busca
```

### 2. Configure environment variables

Create a `.env` file in the project root with the following variables:

```env
# REQUIRED - OpenAI Configuration
OPENAI_API_KEY=your_api_key_here

# REQUIRED - Database Configuration
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/rag
PG_VECTOR_COLLECTION_NAME=documents

# REQUIRED - PDF Configuration
PDF_FILENAME=document.pdf

# OPTIONAL - OpenAI Configuration (default values)
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
GPT_MODEL=gpt-3.5-turbo

# OPTIONAL - Chunk Configuration (default values)
CHUNK_SIZE=1000
CHUNK_OVERLAP=150

# OPTIONAL - Search Configuration (default values)
TOP_K=10
```

**Required variables:**

- `OPENAI_API_KEY`: Your OpenAI API key
- `DATABASE_URL`: PostgreSQL connection URL
- `PG_VECTOR_COLLECTION_NAME`: Vector database collection name
- `PDF_FILENAME`: PDF file name to be processed (must be in project root)

**Optional variables** (have default values):

- `OPENAI_EMBEDDING_MODEL`: Embedding model (default: text-embedding-3-small)
- `GPT_MODEL`: Chat model (default: gpt-3.5-turbo)
- `CHUNK_SIZE`: Text chunk size (default: 1000)
- `CHUNK_OVERLAP`: Overlap between chunks (default: 150)
- `TOP_K`: Number of search results (default: 10)

### 3. Add the PDF file

**IMPORTANT:** The PDF file must be in the **project root** (same directory as `README.md`).

```
mba-ia-desafio-ingestao-busca/
├── document.pdf          ← PDF must be here
├── README.md
├── docker-compose.yml
└── src/
```

Make sure that:

- The PDF file exists in the project root
- The filename matches the `PDF_FILENAME` value in the `.env` file
- The file is not corrupted and can be read

### 4. Install Python dependencies

```bash
# Activate virtual environment (if exists)
source venv/bin/activate

# Or create a new virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 🐳 Docker Execution

### 1. Start database services

```bash
docker-compose up -d
```

This command will:

- Start PostgreSQL with pgvector on port 5432
- Automatically configure the vector extension
- Start Adminer on port 8080 for database administration

### 2. Check if services are running

```bash
docker-compose ps
```

### 3. Access Adminer (optional)

Open http://localhost:8080 in your browser to access the database interface:

- **Server**: postgres
- **User**: postgres
- **Password**: postgres
- **Database**: rag

## 📚 Execution Order

### Step 1: Document Ingestion

```bash
cd src
python ingest.py
```

This script will:

- Load the PDF file specified in `PDF_FILENAME`
- Split the document into text chunks
- Generate embeddings using OpenAI
- Store embeddings in PostgreSQL database

**Expected output:**

```
Starting to ingest PDF.
PDF 'document.pdf' was ingested successfully.
```

### Step 2: Start Chat

```bash
cd src
python chat.py
```

This script will:

- Start an interactive chat interface
- Allow asking questions about the document
- Search for relevant information in the vector database
- Generate responses based on the found context

**Expected output:**

```
Chat started! Type 'exit' to quit.
--------------------------------------------------

Your question:
```

## 💬 How to Use the Chat

1. **Ask questions** about the PDF document content
2. **Type 'exit'** to quit the chat
3. **Use Ctrl+C** to interrupt the program

### Example questions:

- "What is the main theme of the document?"
- "What are the most important points?"
- "Explain the concept of [specific term]"
- "Summarize the chapter about [topic]"

## 🔧 Project Structure

```
├── src/
│   ├── common.py          # Shared configurations
│   ├── ingest.py          # Document ingestion script
│   ├── search.py          # Search and generation logic
│   └── chat.py            # Chat interface
├── docker-compose.yml     # Service configuration
├── requirements.txt       # Python dependencies
├── document.pdf          # Document to process
└── README.md             # This file
```

## 🛠️ Troubleshooting

### Database connection error

```bash
# Check if PostgreSQL is running
docker-compose ps

# Restart services if necessary
docker-compose restart
```

### API Key error

- Verify that `OPENAI_API_KEY` is correct in the `.env` file
- Confirm that the API key has available credits

### PDF file error

- **Check if the PDF file is in the project root** (same directory as README.md)
- Confirm that the filename is correct in `PDF_FILENAME`
- Verify that the file is not corrupted
- Make sure the file has read permissions

### Clear database data

```bash
# To completely restart
docker-compose down -v
docker-compose up -d
```

## 📊 Monitoring

### Container logs

```bash
docker-compose logs -f postgres
```

### Check database data

```sql
-- Connect via Adminer or psql
SELECT COUNT(*) FROM langchain_pg_collection;
SELECT * FROM langchain_pg_embedding LIMIT 5;
```

## 🎯 Features

- ✅ **Automatic ingestion** of PDF documents
- ✅ **Semantic search** using vector embeddings
- ✅ **Interactive chat** with contextual responses
- ✅ **Complete containerization** with Docker
- ✅ **Administrative interface** with Adminer
- ✅ **Flexible configuration** via environment variables

## 📝 Important Notes

- The system responds **only** based on the PDF document content
- If the information is not in the document, it will return: "I don't have the necessary information to answer your question"
- The default embedding model is `text-embedding-3-small`
- The default chat model is `gpt-3.5-turbo`

## 🤝 Contributing

To contribute to the project:

1. Fork the repository
2. Create a branch for your feature
3. Commit your changes
4. Open a Pull Request

## 📄 License

This project was developed as part of the MBA Software Engineering with AI challenge from Full Cycle.
