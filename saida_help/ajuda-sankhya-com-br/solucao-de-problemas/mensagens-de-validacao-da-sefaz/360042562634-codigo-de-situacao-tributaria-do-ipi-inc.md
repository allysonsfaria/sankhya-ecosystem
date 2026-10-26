---
id: "360042562634"
titulo: "Código de Situação Tributária do IPI incompatível com o Código de Enquadramento Legal do IPI [nItem:nnn] (NT2015/002)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042562634-C%C3%B3digo-de-Situa%C3%A7%C3%A3o-Tribut%C3%A1ria-do-IPI-incompat%C3%ADvel-com-o-C%C3%B3digo-de-Enquadramento-Legal-do-IPI-nItem-nnn-NT2015-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:45Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "388", "Verificar enquadramento e CST", "Ajustar cadastros refazer nota", "Código IPI incompatível"]
---

# Código de Situação Tributária do IPI incompatível com o Código de Enquadramento Legal do IPI [nItem:nnn] (NT2015/002)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16475217825943) MENSAGEM:**

[388 - Rejeição]: Código de Situação Tributária do IPI incompatível com o Código de Enquadramento Legal do IPI [nItem:nnn] (NT2015/002).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16475173013783) SOLUÇÃO:**

Verifique se o código de enquadramento do IPI foi devidamente informado nos cadastros informados abaixo. Caso tenha informado, verifique se o código informado é compatível com o CST de IPI.

A Sefaz realiza a validação da seguinte forma:

- Para os CSTs 02 e 52 – Isenção de IPI, o código de enquadramento deve ser entre 301 e 399
- Para os CSTs 04 e 54 – Imunidade de IPI, o código de enquadramento deve ser entre 001 e 099
- Para os CSTs 05 e 55 – Suspensão de IPI, o código de enquadramento deve ser entre 101 e 199
- Lembrando que o código informado deverá constar na lista do Anexo XIV - Código de Enquadramento Legal do IPI da NT 2015/002.

**![Imagem 3: IMPORTANTE :](https://ajuda.sankhya.com.br/hc/article_attachments/16475173018775) IMPORTANTE:**

Após ajustes nos cadastros, recomendamos que a nota seja inutilizada e o lançamento refeito.

**Regras do sistema para buscar a CST de IPI e o Código de Enquadramento Legal do IPI:**

(1)** Venda:**

![Imagem 4: Top - " Tipo de operação " (Caminho de acesso: Comercial » Arquivo » Cadastros )](https://ajuda.sankhya.com.br/hc/article_attachments/16475217833111) Top - "**[Tipo de operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** (Caminho de acesso: Comercial » Arquivo » Cadastros)

**"Tem IPI?"**

- Não: pega a CST de Saída e Código de Enquadramento Legal do IPI informada neste cadastro.
- Sim: passa para o próximo cadastro.

![Imagem 5: Cadastro de " Produtos " ( Caminho de acesso: Configurações » Cadastros » Produtos )](https://ajuda.sankhya.com.br/hc/article_attachments/16475173024919) Cadastro de ["**Produtos**"  (](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)Caminho de acesso: Configurações » Cadastros » Produtos)

  **"Tem IPI na Venda?"**

- Não: pega a CST de Saída e Código de Enquadramento Legal do IPI informada neste cadastro.

     - Sim: passa para o próximo cadastro.   

![Imagem 6: " Empresa " - Preferências da empresa (Caminho de acesso: Comercial » Preferências )](https://ajuda.sankhya.com.br/hc/article_attachments/16475173027863) "[**Empresa**"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)- Preferências da empresa (Caminho de acesso: Comercial » Preferências)

**"Tem IPI?"**

     - Não: pega a CST de Saída e Código de Enquadramento Legal do IPI informada neste cadastro.

     -  Sim: passa para o próximo cadastro.   

![Imagem 7: Cadastro de "Parceiros" (Caminho de acesso: Configurações » Cadastros )](https://ajuda.sankhya.com.br/hc/article_attachments/16475173030039) Cadastro de **["Parceiros"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)** (Caminho de acesso: Configurações » Cadastros)

**"Tem IPI?"**

- Não: pega a CST de Saída e Código de Enquadramento Legal do IPI informada neste cadastro.
- Sim: passa para o próximo cadastro.

![Imagem 8: Cadastro das " Alíquotas de IPI" (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas )](https://ajuda.sankhya.com.br/hc/article_attachments/16475173034135) Cadastro das "[**Alíquotas de IPI"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013) (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas)

     - Faz o cálculo e pega a CST de saída e Código de Enquadramento Legal do IPI informado neste cadastro

(1)** Compra:**

![Imagem 9: Top - Tipo de operação](https://ajuda.sankhya.com.br/hc/article_attachments/16475217833111) Top - Tipo de operação

**"Tem IPI?"**

- Não: pega a CST de ENTRADA e Código de Enquadramento Legal do IPI  informada neste cadastro.
- Sim: passa para o próximo cadastro.

![Imagem 10: Cadastro de produtos](https://ajuda.sankhya.com.br/hc/article_attachments/16475173024919) Cadastro de produtos

**"Tem IPI na Compra?"**

- Não: pega a CST de ENTRADA e Código de Enquadramento Legal do IPI informada neste cadastro.
- Sim: passa para o próximo cadastro.

![Imagem 11: Cadastro de parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/16475173027863) Cadastro de parceiros

  **"Tem IPI?"**

     - Não: pega a CST de ENTRADA e Código de Enquadramento Legal do IPI informada neste       cadastro.

     -  Sim: passa para o próximo cadastro.   

![Imagem 12: Cadastro de alíquotas de IPI](https://ajuda.sankhya.com.br/hc/article_attachments/16475173030039) Cadastro de alíquotas de IPI

- Faz o cálculo e pega a CST de ENTRADA e Código de Enquadramento Legal do IPI informada neste cadastro.

**![Imagem 13: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16475173036567) CAUSA:**

Quando for emitida uma NF-e e o Código de Enquadramento Legal do IPI (cEnq) não for compatível com o CST será retornado a rejeição.

**![Imagem 14: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16475173037975) OBSERVAÇÕES:**

**(1)** Este campo é histórico na tabela de Itens. Se for necessário corrigir algum cadastro no sistema também será necessário excluir o item e incluir novamente na grade de itens dos portais. Ou se a Nota é originada a partir de um Pedido de Venda, deverá ajustar a TOP de Pedido para o correto cálculo do imposto e posteriormente faturá-lo.

**(1)** ([NT2015/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=hDS5co/qWOc=)) - Nota Técnica.

**(1)** No XML: Os campos associados a essa validação são: <cEnq> e <CST>, dentro do Grupo <IPI>.

<IPI>
    <cEnq>999</cEnq>
    <IPINT>
        <CST>55</CST>
    </IPINT>
</IPI>
