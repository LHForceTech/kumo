# Builder

A seção **`builder`** define comportamentos para o build da aplicação:
   - **`multiarch`**: Define se o build suporta múltiplas arquiteturas (true ou false).
   - **`dockerfile`** e **`context`**: Referem-se ao arquivo Dockerfile e ao contexto de build.
   - **`use_buildx`**: Indica se deve usar o `docker buildx` para builds avançados.
   - **`versioning`** e **`environment`**: Controle de versão (baseado em hash neste caso) e ambiente de execução.
   - **`arch`**: Lista de arquiteturas suportadas (ex.: `linux/amd64`, `linux/arm64`).
   - **`args`**: Variáveis de build para o Docker, como `VAR_1`.

