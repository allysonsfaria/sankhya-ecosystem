---
id: "360043421933"
titulo: "Para TOP configurada como NF-e a numeração da nota deve ser automática"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043421933-Para-TOP-configurada-como-NF-e-a-numera%C3%A7%C3%A3o-da-nota-deve-ser-autom%C3%A1tica"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:58Z"
rotulos: ["#PUBLIFER", "CORE_E01858", "Configuração", "Impressão", "NF-e", "TOP", "Configure TOP para numeração automática", "NF-e exige numeração automática", "TOP não está configurada corretamente", "Documentos Eletrônicos"]
---

# Para TOP configurada como NF-e a numeração da nota deve ser automática

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16117788777367) MENSAGEM:**

[CORE\_E01858] Para TOP configurada como NF-e a numeração da nota deve ser automática.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16117772165527) SOLUÇÃO:**

Considerando a emissão de nota fiscal eletrônica, na qual o número nota é gerado de forma sequencial pelo sistema, realize devidamente a marcação abaixo:

![Imagem 3: Acesse a tela " Tipos de Operação-TOP " (Caminho de acesso: Comercial » Arquivo » Cadastros).](https://ajuda.sankhya.com.br/hc/article_attachments/16117788782103) Acesse a tela **"[Tipos de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** (Caminho de acesso: Comercial » Arquivo » Cadastros).

![Imagem 4: Selecione a TOP utilizada no respectivo lançamento e na aba "Impressão" , marque o campo ' Numeração somente automática…](https://ajuda.sankhya.com.br/hc/article_attachments/16117772169111) Selecione a TOP utilizada no respectivo lançamento e na aba **"Impressão"**, marque o campo '**Numeração somente automática**';

| Após fazer o ajuste mencionado (conforme imagem abaixo), lembre-se de forçar a **atualização dessa informação em seu lançamento**. Sugerimos que troque a TOP do cabeçalho da nota, salve a alteração, em seguida volte para a TOP correta. |
| --- |

![Imagem 5: Após fazer o ajuste mencionado (conforme imagem abaixo), lembre-se de forçar a atualização dessa informação em seu…](https://ajuda.sankhya.com.br/hc/article_attachments/14610531126423)

**(2)** Caso o procedimento de forçar a troca da TOP não solucione, refaça o lançamento/faturamento;

**![Imagem 6: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17804097623319) IMPORTANTE:**

| Caso esteja realizando o lançamento de uma **nota emitida por Terceiros** e a numeração de fato NÃO deva ser automática, será necessário ajustar a configuração do campo "**NF-e"** da aba **"Impressão"** para **"Terceiros"**. |
| --- |

**![Imagem 7: Caso esteja realizando o lançamento de uma nota emitida por Terceiros e a numeração de fato NÃO deva ser automática,…](https://ajuda.sankhya.com.br/hc/article_attachments/16117788797463) OBSERVAÇÕES**:

**(2)**Se o parâmetro **"Valida config. de Nr automática** na **TOP-VALNRAUTTOP**" estiver ligado, ao criar ou alterar uma TOP de Venda ou Compra, com o campo NF-e diferente de Convencional (Não Usa NF-e), Import. Doc. (Emissão Própria) e Terceiros, na aba **"Impressão"** a marcação **"Numeração somente automática"** deverá estar selecionada e o campo **"Base de Numeração"** deverá indicar a opção **"Venda"** ou **"Devolução de venda"**.

**(2)**Caso não esteja marcada, ao tentar salvar a configuração o sistema apresentará a seguinte mensagem:

**(3)**“Para TOP Configurada com Modelo de Documento 55 - Nota Fiscal Eletrônica e o campo NF-e diferente de ‘Convencional (Não Usa NF-e)', ‘Import. Doc.(Emissão Própria)' e 'Terceiros’ a numeração da Nota deve ser automática". Marque a opção **"Numeração somente automática"** e use a **"base de numeração"** Venda ou Devolução de venda".

**![Imagem 8: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16117772186135) CAUSA**:

Mensagem será apresentada ao realizar emissão de nota fiscal eletrônica, utilizando um tipo de operação com a configuração não definida com 'numeração somente automática';
