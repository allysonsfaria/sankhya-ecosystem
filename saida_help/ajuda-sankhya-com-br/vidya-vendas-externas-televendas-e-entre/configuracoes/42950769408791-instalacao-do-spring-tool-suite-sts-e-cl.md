---
id: "42950769408791"
titulo: "Instalação do Spring Tool Suite (STS) e Clonagem de Projeto via Git"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950769408791-Instala%C3%A7%C3%A3o-do-Spring-Tool-Suite-STS-e-Clonagem-de-Projeto-via-Git"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Configurações"
atualizado_em: "2026-09-18T23:23:27Z"
rotulos: ["sync_hc", "vidya", "vidya_600128", "sync_hash_161fc4f90c48"]
---

# Instalação do Spring Tool Suite (STS) e Clonagem de Projeto via Git

## 1. Objetivo

Este artigo mostra o passo a passo para instalar o **Spring Tool Suite (STS)** — a IDE baseada em Eclipse voltada para desenvolvimento Spring/Java — e, em seguida, clonar (baixar) o repositório de um projeto hospedado no GitHub diretamente por dentro da ferramenta, deixando o ambiente pronto para desenvolvimento.

## 2. Pré-requisitos

- Acesso à internet.
- Conta no **GitHub** com permissão de acesso ao repositório da organização (ex.: convite aceito para a organização do projeto).
- Java (JDK) instalado na máquina, necessário para rodar o STS e compilar os projetos Maven/Java.

## 3. Passo 1 — Baixar o Spring Tool Suite

1. Acesse o site oficial: **spring.io/tools**.
2. Role a página até a seção **"Spring Tools for Eclipse"** (existem também as opções "for Visual Studio Code" e "for Theia", mas o processo abaixo é para a versão Eclipse).
3. Escolha o pacote de acordo com o sistema operacional e arquitetura da máquina, por exemplo:
   - `4.30.0 - LINUX X86_64`
   - `4.30.0 - LINUX ARM_64`
   - `4.30.0 - MACOS X86_64`
   - `4.30.0 - MACOS ARM_64`
   - Ou a opção equivalente para **Windows** (ex.: `WIN32.WIN32.X86_64`), rolando um pouco mais a página.
4. Clique na versão desejada para iniciar o download do arquivo `.zip` (ex.: `spring-tools-for-eclipse-4.30.0.RELEASE-e4.35.0-win32.win32.x86_64.zip`).

## 4. Passo 2 — Extrair o arquivo baixado

1. Localize o `.zip` baixado na pasta **Downloads**.
2. Extraia todo o conteúdo (é um pacote grande, com milhares de arquivos — a extração pode levar alguns minutos).
3. Dentro da pasta extraída (ex.: `sts-4.30.0.RELEASE`) você verá, entre outros itens:
   - Pastas: `configuration`, `dropins`, `features`, `p2`, `plugins`, `readme`
   - `SpringToolSuite4.exe` → executável principal da IDE
   - `SpringToolSuite4c.exe` → variante "console" do executável
   - `SpringToolSuite4.ini` → arquivo de configuração/parâmetros de inicialização

## 5. Passo 3 — Primeira execução do STS

1. Dê duplo clique em **`SpringToolSuite4.exe`**.
2. Aguarde a tela de carregamento **"Spring Tools"** (Tanzu) finalizar.
3. A IDE abrirá com um workspace padrão (ex.: `workspace-spring-tools-for-eclipse-4.30.0.RELEASE`).
4. No **Package Explorer**, como ainda não há nenhum projeto, aparecerão as opções:
   - Create a Java project
   - Create a Maven project
   - Create new Spring Starter Project
   - Import Spring Getting Started Content
   - Create a project...
   - **Import projects...** ← é essa opção que vamos usar para trazer o projeto do Git

## 6. Passo 4 — Clonar o repositório do projeto

1. Clique em **Import projects...**
2. Na aba/visão **Git Repositories**, selecione **"Clone a Git repository"**.
3. Na janela **Clone Git Repository**, preencha:
   - **URI**: endereço HTTPS do repositório no GitHub (ex.: `https://github.com/<organização>/<nome-do-repositorio>`)
   - **Host** e **Repository path**: são preenchidos automaticamente a partir da URI
   - **Protocol**: `https`
   - **User**: seu usuário do GitHub
   - **Password**: **não é a senha da sua conta** — veja o Passo 5 abaixo sobre como gerar o token de acesso
4. Clique em **Next** e siga o assistente (seleção de branch, pasta de destino local, etc.) até **Finish**.

> Dica: marque **"Store in Secure Store"** se quiser que o STS lembre a credencial e não peça o token novamente nas próximas operações de Git.

## 7. Passo 5 — Gerar o Personal Access Token no GitHub

O GitHub não aceita mais a senha normal da conta para operações de Git via HTTPS — é necessário um **Personal Access Token (classic)**:

1. No navegador, acesse **github.com** e faça login.
2. Vá em **Settings** (configurações da conta).
3. No menu, acesse **Developer settings** → **Personal access tokens** → **Tokens (classic)**.
4. Clique em **Generate new token** (Generate new token classic).
5. Selecione os **escopos (scopes)** necessários — no mínimo o escopo de acesso a repositórios (`repo`), para permitir clonar/enviar código.
6. Clique em **Generate token**.
7. **Copie o token imediatamente** e guarde em um local seguro (ex.: um bloco de notas temporário) — o GitHub mostra o valor **apenas uma vez**; se perder, será necessário gerar um novo.
8. Volte para a janela **Clone Git Repository** do STS e cole esse token no campo **Password**.

## 8. Passo 6 — Concluir a clonagem

1. Com usuário e token preenchidos, clique em **Next** novamente.
2. Confirme a branch a ser clonada (normalmente `main` ou `master`) e o diretório local de destino.
3. Clique em **Finish**.
4. O STS vai baixar o repositório e importar o projeto automaticamente no **Package Explorer** (geralmente como projeto Maven, exibindo `pom.xml` e os pacotes/classes Java).

## 9. Passo 7 — Liberar o Firewall do Windows (quando necessário)

Ao rodar a aplicação importada pela primeira vez (por exemplo, ao iniciar o projeto Spring Boot dentro do STS), o Windows pode exibir o aviso:

> **Segurança do Windows** — "Deseja permitir que redes públicas e privadas acessem este aplicativo?" O Firewall do Windows bloqueou alguns recursos de `SpringToolSuite4.exe` (ou do processo Java/OpenJDK) em todas as redes públicas ou privadas.

Basta clicar em **Permitir acesso** para que a aplicação consiga subir e se comunicar normalmente (ex.: subir o servidor local da API).

## 10. Resultado esperado

Ao final do processo você terá:

- O Spring Tool Suite instalado e funcional.
- O repositório do projeto clonado localmente e já importado como projeto Maven/Java dentro da IDE.
- Ambiente pronto para rodar, depurar e desenvolver a aplicação.

## 11. Observações

- Guarde o Personal Access Token com cuidado — ele funciona como uma senha e não deve ser compartilhado.
- Caso o token expire ou seja perdido, repita o Passo 5 para gerar um novo.
- Se aparecerem múltiplos avisos de firewall (ex.: para `OpenJDK Platform binary`), permita o acesso da mesma forma — normalmente ocorre a cada novo processo Java iniciado, especialmente após updates da JDK.
