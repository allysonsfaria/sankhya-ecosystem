---
id: "39266413296023"
titulo: "Web Connection não é iniciado automaticamente após reinicialização do computador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39266413296023-Web-Connection-n%C3%A3o-%C3%A9-iniciado-automaticamente-ap%C3%B3s-reinicializa%C3%A7%C3%A3o-do-computador"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T13:59:29Z"
rotulos: ["Produtos", "Configuração", "Segurança", "Implementação e Configuração do Sankhya Web Connection", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Plataforma - KCS", "Windows"]
---

# Web Connection não é iniciado automaticamente após reinicialização do computador

**MENSAGEM:**

O Web Connection não é iniciado automaticamente após reinicialização do computador.

E todas as vezes tem que fazer o processo manual de iniciar o Web Connection.

**SOLUÇÃO:**

Validar se o arquivo de inicialização (.bat) existe na pasta:

```
C:\Users\usuario\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

ou acessando via "executar" digite:

```
shell:startup
```

Caso o arquivo não exista:

1. Reinstalar o **Web Connection** com privilégios de administrador.
   **ou**
2. Refazer o processo via login administrador e fazer a instalação.
3. Após a instalação validar a pasta abaixo onde o .bat aparecerá:

![Imagem 1: Após a instalação validar a pasta abaixo onde o .bat aparecerá:](https://ajuda.sankhya.com.br/hc/article_attachments/39266413285783)

Caso o arquivo exista, mas não execute:

- Verificar bloqueios de **antivírus** ou **firewall**
- Criar exceções para o Web Connection e para o script `.bat`

Reiniciar a máquina e validar se o serviço inicia automaticamente.

![Imagem 2: Reiniciar a máquina e validar se o serviço inicia automaticamente.](https://ajuda.sankhya.com.br/hc/article_attachments/39266413286679)

**CAUSA:**

O problema pode ocorrer, principalmente, por dois motivos:

- O instalador do **Web Connection** não criou corretamente o arquivo de inicialização na pasta de startup do Windows:
- ```
  C:\Users\usuario\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
  ```

ou

- Existência de **restrições de segurança**, como antivírus ou firewall ou ate mesmo acessos administradores, que impedem a execução automática do serviço.
