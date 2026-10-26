---
id: "39358019354647"
titulo: "Nomenclatura Divergente TRCT - Suspensão Vindo como Outros Descontos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39358019354647-Nomenclatura-Divergente-TRCT-Suspens%C3%A3o-Vindo-como-Outros-Descontos"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:23:00Z"
rotulos: ["Configuração", "Eventos", "Relatórios", "Pessoal+", "TRCT", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Nomenclatura Divergente TRCT - Suspensão Vindo como Outros Descontos

**Situação**

Ao emitir o **"Termo de Rescisão de Contrato de Trabalho (TRCT)"**, os eventos personalizados aparecem com nomenclaturas divergentes das desejadas. Por exemplo, um evento configurado como **"Suspensão"** ou outro desconto específico está sendo exibido como **"Outros Descontos"** no relatório, causando confusão na visualização do colaborador e dificultando a identificação correta dos valores.

**Causa**

A nomenclatura divergente ocorre porque os eventos personalizados não foram configurados adequadamente na aba **"TRCT"** da tela **"Regras de Cálculo"** (Pessoal+ » Cadastros » Regras de Cálculo). Quando um evento é criado, ele pode ser vinculado a campos genéricos do TRCT (como **"Outros Descontos"** - campo 115), mas sem uma descrição personalizada específica. Isso faz com que o sistema utilize a nomenclatura padrão do campo ao invés do nome desejado para o evento.

Para que o relatório apresente as informações de forma clara e personalizada, é necessário configurar manualmente cada evento na regra de cálculo correspondente, inserindo a nomenclatura que melhor identifique o desconto ou provento para o colaborador.

**Solução**

Para alterar a nomenclatura dos eventos personalizados no TRCT, execute os passos abaixo:

**(1)**  Acesse a tela **"Regras de Cálculo"** (Pessoal+ » Cadastros » Regras de Cálculo). 

**(2)**  Clique na aba **"TRCT"** para visualizar os campos configurados para o relatório de rescisão.

![Imagem 1: (1) Acesse a tela "Regras de Cálculo" (Pessoal+ » Cadastros » Regras de Cálculo). (2) Clique na aba "TRCT" para…](https://ajuda.sankhya.com.br/hc/article_attachments/41275408559127)

![Imagem 2: (1) Acesse a tela "Regras de Cálculo" (Pessoal+ » Cadastros » Regras de Cálculo). (2) Clique na aba "TRCT" para…](https://ajuda.sankhya.com.br/hc/article_attachments/41275403594391)

**(3)**  Localize o evento personalizado que deseja renomear. Utilize a busca para facilitar a localização, caso necessário. 

**(4)**  No campo correspondente ao evento, insira a nova nomenclatura desejada (por exemplo, altere de **"Outros"** para **"Desconto Unimed"** ou **"Suspensão"**).

![Imagem 3: Salve as alterações realizadas na "Regras de Cálculo" . Emita novamente o "TRCT" para verificar se a nomenclatura foi…](https://ajuda.sankhya.com.br/hc/article_attachments/41275403594391)

**(5)**  Salve as alterações realizadas na **"Regras de Cálculo"**. 

**(6)**  Emita novamente o **"TRCT"** para verificar se a nomenclatura foi atualizada corretamente no relatório.
