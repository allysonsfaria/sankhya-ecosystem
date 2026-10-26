---
id: "10084925338135"
titulo: "O ambiente SEFAZ no momento não se encontra em operação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10084925338135-O-ambiente-SEFAZ-no-momento-n%C3%A3o-se-encontra-em-opera%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-10-08T20:08:45Z"
rotulos: ["MDF-e", "Configuração", "SEFAZ", "CORE_E03545", "Ambiente SEFAZ Indisponível para MDF-e", "Erro", "Documentos Eletrônicos"]
---

# O ambiente SEFAZ no momento não se encontra em operação

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19298251113239) MENSAGEM:**

[CORE\_E03545] O ambiente SEFAZ no momento não se encontra em operação. Tente novamente mais tarde ou se for o caso opte por Gerar o MDF-e em Contingência.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19298296109975) SITUAÇÃO:**

Ao tentar transmitir um MDF-e a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19298251123351) CAUSA:**

Poderá ocorrer por configuração incorreta do campo "Ambiente MDF-e" ou instabilidade do ambiente da SEFAZ.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19298251128727) SOLUÇÃO:**

Acesse as preferências da **Empresa** (Caminho de acesso à tela: Comercial » Preferências » Empresa), vá ate a aba MDF-e e veja como está a configuração do campo "Ambiente MDF-e".

![Imagem 5: Acesse as preferências da Empresa (Caminho de acesso à tela: Comercial » Preferências » Empresa), vá ate a aba MDF-e e…](https://ajuda.sankhya.com.br/hc/article_attachments/19298296119831)

Determina-se no "Ambiente MDF-e" qual o âmbito de emissão de MDF-e que a empresa se encaixa; tem-se as seguintes opções:

- **Não usa:** A empresa não faz uso de MDF-e;
- **Homologação:** Os MDF-e's emitidos pela empresa em questão, são válidos apenas para testes e simulações;
- **Produção:** Por esta opção, tem-se que a empresa gera efetivamente MDF-e's e estes serão devidamente validados pelos órgãos competentes.

Caso o campo já esteja configurado corretamente é necessário verificar se realmente o ambiente da SEFAZ está em operação.
