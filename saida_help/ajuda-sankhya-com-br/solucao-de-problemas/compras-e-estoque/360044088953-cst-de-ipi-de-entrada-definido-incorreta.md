---
id: "360044088953"
titulo: "CST de IPI de entrada definido incorretamente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044088953-CST-de-IPI-de-entrada-definido-incorretamente"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:01:36Z"
rotulos: ["CORE_E04479", "Configuração", "IPI", "Impostos", "TOP", "[CORE_E04479] C.S.T. IPI de Entrada definido incorretamente."]
---

# CST de IPI de entrada definido incorretamente

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16107621769751) MENSAGEM:**

[CORE\_E04479] C.S.T. IPI de Entrada definido incorretamente.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16107621772823) SOLUÇÃO:**

Identifique, de acordo com a hierarquia utilizada pelo sistema e detalhada abaixo, qual o CST IPI está sendo buscado para o lançamento atual:

![Imagem 3: Tela " Tipos de Operação (TOP) " » Aba "Impostos" » Campo "Tem IPI?":](https://ajuda.sankhya.com.br/hc/article_attachments/16107621774231) Tela **"[Tipos de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** » Aba **"Impostos"** » Campo **"Tem IPI?":**

**(2)** Desmarcado: Buscará a  CST de Entrada informada neste cadastro.

**(2)** Marcado: Passa para o próximo cadastro.

![Imagem 4: (2) Marcado: Passa para o próximo cadastro.](https://ajuda.sankhya.com.br/hc/article_attachments/14525771289623)

![Imagem 5: Tela " Produtos " » Aba "Impostos" » Campo "Tem IPI na Compra?" :](https://ajuda.sankhya.com.br/hc/article_attachments/16107603128727) Tela **"[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)"** » Aba **"Impostos"** » Campo **"Tem IPI na Compra?"**:

**(2)** Desmarcado:  Buscará a CST de Entrada informada neste cadastro.

**(2)** Marcado: Passa para o próximo cadastro.

![Imagem 6: (2) Marcado: Passa para o próximo cadastro.](https://ajuda.sankhya.com.br/hc/article_attachments/14525807714327)

![Imagem 7: Tela " Empresa " (Comercial/Preferências) » Aba "Propriedades" » Campo "Trabalha com IPI? ":](https://ajuda.sankhya.com.br/hc/article_attachments/16107621786903) Tela **"[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)"** (Comercial/Preferências) » Aba **"Propriedades"** » Campo **"Trabalha com IPI?**":

**(2)** Desmarcado: Buscará a CST de Entrada informada neste cadastro.

**(2)** Marcado: Passa para o próximo cadastro.

![Imagem 8: Tela " Parceiro " » Aba "Fiscal" » Campo "TEM IPI?":](https://ajuda.sankhya.com.br/hc/article_attachments/16107603139991) Tela **"[Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)"** » Aba **"Fiscal"** » Campo **"TEM IPI?":**

**(2)** Desmarcado: Buscará a CST de Entrada informada neste cadastro.

**(2)** Marcado: Passa para o próximo cadastro.

![Imagem 9: Tela " Alíquota de IPI " :](https://ajuda.sankhya.com.br/hc/article_attachments/16107603141399) Tela **"[Alíquota de IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI)"**:

De acordo com as configurações dessa rotina o sistema realiza o cálculo e caso todas as opções acima estejam marcadas buscará a CST de entrada informada neste cadastro.

Realizada a identificação de qual dos cadastros está sendo utilizado para enviar o CST IPI de Entrada, realize os ajustes, com apoio do seu Contador, de forma que seja enviado um código compatível com a operação/lançamento.

| **Código** | **Descrição** |
| --- | --- |
| 00 | Entrada com Recuperação de Crédito |
| 01 | Entrada Tributável com Alíquota Zero |
| 02 | Entrada Isenta |
| 03 | Entrada Não-Tributada |
| 04 | Entrada Imune |
| 05 | Entrada com Suspensão |
| 49 | Outras Entradas |

**![Imagem 10: Outras Entradas](https://ajuda.sankhya.com.br/hc/article_attachments/16107603148311) CAUSA:**

Mensagem retornada na emissão de nota fiscal eletrônica, quando o CST IPI for definido incorretamente.
