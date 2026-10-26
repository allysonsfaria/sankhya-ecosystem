---
id: "360043871734"
titulo: "Modelo padrão de impressão de OS Portal e FAP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043871734-Modelo-padr%C3%A3o-de-impress%C3%A3o-de-OS-Portal-e-FAP"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:58:01Z"
rotulos: ["Configuração", "Impressão", "FAP", "Relatórios", "Ordem de Serviço", "Portal", "Modelo padrão para impressão"]
---

# Modelo padrão de impressão de OS Portal e FAP

**(1)** Os modelos são padrões que podem ser utilizados para impressão de OS via Portal e FAP seguem:

**(2)** Os modelos abaixo são para impressão de OS via Portal

**osPortal.jrxml**

**osPortal\_itens\_ossub.jrxml**

**(2)** Os modelos abaixo são para impressão de Projeto(FAP).

**projeto.jrxml**
**projeto\_etapas.jrxml**
**projeto\_produtos.jrxml**

![Imagem 1: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16840514672791) Acesse: Configurações » Avançado » Preferências

Parâmetro: **"SERVDIRMOD-Pasta de modelos para impressão"**

- No campo **"Texto"** deste parâmetro identifique o diretório do servidor de aplicação em que o Jboss/WildFly está instalado;
- Insira os arquivos na pasta/diretório;
- Reinicie o servidor de aplicação;
- Efetue a impressão.

**![Imagem 2: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16840506451991) OBSERVAÇÃO:**

O sistema imprime o que tiver no diretório do SERVDIRMOD, senão ele imprime o padrão. Visto via fonte que o sistema olha para o arquivo com o nome igual ao que foi mencionado no help,
**Exemplo:** os.jrxml se tiver diferente o sistema imprime o padrão.

(1)** Anexo abaixo:**
