---
id: "360043361933"
titulo: "CST de IPI de saída definido incorretamente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043361933-CST-de-IPI-de-sa%C3%ADda-definido-incorretamente"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:28Z"
rotulos: ["CORE_E04480", "Configuração", "IPI", "Impostos", "TOP", "Verifique configurações", "CST IPI incorreto", "Ajuste conforme orientações"]
---

# CST de IPI de saída definido incorretamente

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16115298038679) **MENSAGEM:**

[CORE\_E04480] C.S.T. IPI de Saída definido incorretamente.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16115298044951) SOLUÇÃO:**

Identifique, de acordo com a hierarquia utilizada pelo sistema e detalhada abaixo, qual o CST IPI está sendo buscado para o lançamento atual:

**![Imagem 3: Identifique, de acordo com a hierarquia utilizada pelo sistema e detalhada abaixo, qual o CST IPI está sendo buscado…](https://ajuda.sankhya.com.br/hc/article_attachments/16115298047127) "[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** » Aba **"Impostos"** » **"Tem IPI?"**

DESMARCADO: Buscará a  CST de Saída informada neste cadastro.
MARCADO: Passa para o próximo cadastro.

![Imagem 4: " Produtos " » Aba "Impostos" » "Tem IPI na Venda?" DESMARCADO: Buscará a CST de Saída informada neste cadastro.…](https://ajuda.sankhya.com.br/hc/article_attachments/16115298052119) **"[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)"** » Aba **"Impostos"** » **"Tem IPI na Venda?"**
DESMARCADO:  Buscará a CST de Saída informada neste cadastro.
MARCADO: Passa para o próximo cadastro.

**![Imagem 5: " Empresa " (Comercial » Preferências) » Aba "Propriedades" » "Trabalha com IPI?" DESMARCADO: Buscará a CST de Saída…](https://ajuda.sankhya.com.br/hc/article_attachments/16115305696151) "[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)"** (Comercial » Preferências) » Aba **"Propriedades"** » **"Trabalha com IPI?"**
DESMARCADO: Buscará a CST de Saída informada neste cadastro.
MARCADO: Passa para o próximo cadastro.

![Imagem 6: " Parceiro " » Aba "Fiscal" » "TEM IPI?" DESMARCADO: Buscará a CST de Saída informada neste cadastro. MARCADO: Passa…](https://ajuda.sankhya.com.br/hc/article_attachments/16115298057879) **"[Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)"** » Aba **"Fiscal"** » **"TEM IPI?"**
DESMARCADO: Buscará a CST de Saída informada neste cadastro. 
MARCADO: Passa para o próximo cadastro.

**![Imagem 7: " Alíquotas de IPI " De acordo com as configurações dessa rotina o sistema realiza o cálculo e caso todas as opções…](https://ajuda.sankhya.com.br/hc/article_attachments/16115305700375) "[Alíquotas de IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI)"**
De acordo com as configurações dessa rotina o sistema realiza o cálculo e caso todas as opções acima estejam marcadas pega a CST de saída informada neste cadastro.

![Imagem 8: Realizada a identificação de qual dos cadastros está sendo utilizado para enviar o CST IPI de Saída, realize os…](https://ajuda.sankhya.com.br/hc/article_attachments/17802181136023) Realizada a identificação de qual dos cadastros está sendo utilizado para enviar o CST IPI de Saída, realize os ajustes, com apoio do seu Contador, de forma que seja enviado um código compatível com a operação/lançamento:

| **Código** | **Descrição** |
| --- | --- |
| 50 | Saída Tributada |
| 51 | Saída Tributável com Alíquota Zero |
| 52 | Saída Isenta |
| 53 | Saída Não-Tributada |
| 54 | Saída Imune |
| 55 | Saída com Suspensão |
| 99 | Outras Saídas |

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16115298065047) CAUSA:**

Mensagem retornada na emissão de nota fiscal eletrônica, quando o CST IPI for definido incorretamente.
