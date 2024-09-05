if [ $# -eq 0 ]; then
    clear && uvicorn main:app --host 127.0.0.1 --port 8000
elif [ $1 = "dev" ]; then
    clear && uvicorn main:app --reload
elif [ $1 = "test" ]; then
    clear && pytest
else
    echo "Invalid argument"
fi
