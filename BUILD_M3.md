# Building on Apple M3 Silicon

## Prerequisites
* Update XCode tools.
```bash
xcode-select --install
softwareupdate --all --install
```
* cmake
```
brew install cmake
cmake --version
```
* git
## Build
* clone repo 
```
git clone https://github.com/ggerganov/llama.cpp.git
```
* build forcing arm64 and defaulting to METAL support
```
cd llama.cpp
cmake -B build -DCMAKE_SYSTEM_PROCESSOR=arm64
cmake --build build
```
## Test
See README.md on how to get GGUF models from huggingface using cli.

* start server
```
./build/bin/llama-server -m ~/models/Phi-3-mini-4k-instruct-q4.gguf --port 8080
```
* Open http://127.0.0.1:8080




