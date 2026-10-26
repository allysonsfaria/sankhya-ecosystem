---
id: "360060131793"
titulo: "Navegador Incompatível"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360060131793-Navegador-Incompat%C3%ADvel"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:26:32Z"
rotulos: ["Configuração", "Atualização", "html5", "navegador", "incompativel", "plugin", "path", "flex", "Solução para Navegador Incompatível", "Erro", "Sankhya"]
---

# Navegador Incompatível

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16272768554903) MENSAGEM:**

Navegador Incompatível. Essa tela não é mais compatível com seu navegador. Para continuar utilize o [Navegador Sankhya](http://downloads.sankhya.com.br/downloads?app=WebClient) ou [Navegador Jiva](http://downloads.jiva.com.br/downloads?app=WebClient)

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16272768556055) SOLUÇÃO**:

É possível tratar essa situação de duas maneiras:

| **1- Atualização do sistema;**  **2- Execução do path** (Caso não deseje realizar a atualização do release, é possível optar apenas pelo ajuste mencionado nesse tópico 2); |
| --- |

### 1. Atualização do Sistema:

Caso se depare com a mensagem acima e a versão do sistema esteja entre as versões compiladas **08/10/2020** a **23/11/2020**, **efetue a atualização do sistema**, para a release mais recente. (4.3, 4.4, 4.5 e 4.6).

- **Exemplo**: Se estiver na release **4.5b141** 08/10/2020 22:47, atualize para a última release da 4.5 disponível

**1ª Ação:** Como identificar a data de compilação da versão atual?
Logado no sistema, clique no ícone do Usuário Logado, em seguida sobre a versão 4.Xbxxx

[GIF animado: Imagem 3: 1ª Ação: Como identificar a data de compilação da versão atual? Logado no sistema, clique no ícone do Usuário Logado,…](https://ajuda.sankhya.com.br/hc/article_attachments/360098708094)

**2ª Ação:** Após os ajustes, acesse novamente o sistema com um dos Navegadores compatíveis (Chrome, Firefox ou Edge) ou Navegadores Sankhya/Jiva.

Esta ação, visa instruir aos clientes quanto ao suporte do plugin do Flash que será descontinuado a partir de 01/01/2021. Então, para que a operação dos sistemas Sankhya/Jiva, não seja interrompida, recomendamos que seja feita a atualização do release o quanto antes, a fim de evitar transtornos.

### 2- Execução do path:

O gerenciador de pacotes foi modificado para incluir o patch para correção do bloqueio do flex;

- A versão/build do gerenciador é: **2.3b85**
- O download pode ser feito em:

Sankhya: [http://downloads.sankhya.com.br/downloads?app=instaladores](https://www.google.com/url?q=http://downloads.sankhya.com.br/downloads?app%3Dinstaladores&sa=D&source=hangouts&ust=1606855517097000&usg=AFQjCNF0G9-FtLm5OXrglu0gCUvspCRHcA)

Jiva: <http://downloads.jiva.com.br/downloads?app=instaladores>

- A atualização do gerenciador é manual.

**Passos para executar o patch:**
![Imagem 4: Passos para executar o patch: Parar o sistema (parar o wildfly/jboss); Execute o gerenciador de pacotes; Selecione o…](https://ajuda.sankhya.com.br/hc/article_attachments/16272762232727) Parar o sistema (parar o wildfly/jboss);
![Imagem 5: Passos para executar o patch: Parar o sistema (parar o wildfly/jboss); Execute o gerenciador de pacotes; Selecione o…](https://ajuda.sankhya.com.br/hc/article_attachments/16272762234519) Execute o gerenciador de pacotes;
![Imagem 6: Passos para executar o patch: Parar o sistema (parar o wildfly/jboss); Execute o gerenciador de pacotes; Selecione o…](https://ajuda.sankhya.com.br/hc/article_attachments/16272762235927) Selecione o servidor opção: [2] Selecionar Servidor;
![Imagem 7: Passos para executar o patch: Parar o sistema (parar o wildfly/jboss); Execute o gerenciador de pacotes; Selecione o…](https://ajuda.sankhya.com.br/hc/article_attachments/16272762238231) Selecione o servidor que deseja aplicar o patch (essa opção varia conforme os servidores registrados);
![Imagem 8: Passos para executar o patch: Parar o sistema (parar o wildfly/jboss); Execute o gerenciador de pacotes; Selecione o…](https://ajuda.sankhya.com.br/hc/article_attachments/16272768563095) Selecione a opção de patch: [14] Aplicar patch mensagem flex (correção);
![Imagem 9: Passos para executar o patch: Parar o sistema (parar o wildfly/jboss); Execute o gerenciador de pacotes; Selecione o…](https://ajuda.sankhya.com.br/hc/article_attachments/16272762244503) Inicie o sistema (wildfly/jboss).

Conforme ilustrado abaixo:

![Imagem 10: Passos para executar o patch: Parar o sistema (parar o wildfly/jboss); Execute o gerenciador de pacotes; Selecione o…](https://ajuda.sankhya.com.br/hc/article_attachments/14636500931351)

![Imagem 11: Passos para executar o patch: Parar o sistema (parar o wildfly/jboss); Execute o gerenciador de pacotes; Selecione o…](https://ajuda.sankhya.com.br/hc/article_attachments/14636531552791)

Após concluído, o resultado será:

![Imagem 12: Após concluído, o resultado será:](https://ajuda.sankhya.com.br/hc/article_attachments/360100944613)
