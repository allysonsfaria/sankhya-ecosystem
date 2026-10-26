---
id: "360060231573"
titulo: "Importação Convênio/Movimento – Movimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360060231573-Importa%C3%A7%C3%A3o-Conv%C3%AAnio-Movimento-Movimento"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:26:30Z"
rotulos: ["Configuração", "Eventos", "Movimentação Financeira", "Importação", "Preferências", "não apagar", "#validadoRayssa", "#publicadoHyago", "Problema na Importação de Eventos de Movimento"]
---

# Importação Convênio/Movimento – Movimento

**![Imagem 1: MENSAGEM/DÚVIDA :](https://ajuda.sankhya.com.br/hc/article_attachments/16272953217943) MENSAGEM/DÚVIDA**:

Sistema não está importando corretamente o evento para o movimento quando o código possui 3 dígitos.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16272953221527) SOLUÇÃO:**

Realize o seguinte processo a baixo:

![Imagem 3: Acesse: avançado >> preferências >> todas as preferências, localize o parâmetro " CONSI3DIGEVEN - considerar 3 dig.…](https://ajuda.sankhya.com.br/hc/article_attachments/16272936520471) Acesse: avançado >> preferências >> todas as preferências, localize o parâmetro **"CONSI3DIGEVEN** **- considerar 3 dig. para cod. evento na importação",** assinale o mesmo e confirme.
Em seguida, saia e entre novamente no sistema.

![Imagem 4: Acesse: avançado >> preferências >> todas as preferências, localize o parâmetro " CONSI3DIGEVEN - considerar 3 dig.…](https://ajuda.sankhya.com.br/hc/article_attachments/16272936523671) Realize uma nova importação do arquivo e verifique se os dados ficaram corretos.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16272953238807) CAUSA:**

O problema ocorre quando o parâmetro CONSI3DIGEVEN está desligado.
