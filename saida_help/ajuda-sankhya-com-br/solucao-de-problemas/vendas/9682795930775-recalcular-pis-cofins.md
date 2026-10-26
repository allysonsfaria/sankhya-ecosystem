---
id: "9682795930775"
titulo: "Recalcular PIS/COFINS "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9682795930775-Recalcular-PIS-COFINS"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-24T12:41:57Z"
rotulos: ["Configuração", "Fiscal", "COFINS", "PIS", "Financeiro", "Controle de Acesso", "Função em Portais/Centrais controlada por acessos", "Resumo de Processados/Não Processados confirmação do usuário", "NF-e NFS-e CT-e exceto devolução ou cancelados", "Documentos Eletrônicos"]
---

# Recalcular PIS/COFINS 

**(1)Disponível a partir da versão 4.12.**

Foi colocada uma opção **“Recalcular PIS/COFINS”** em Outras Opções nos Portais e nas Centrais (Compra e Vendas), essa função deverá ser configurado/liberado o controle de acessos individuais por Grupo e por usuário.

![Imagem 1: Para tal, vá até a tela "Controle de Acessos" (Caminho de acesso: Configurações » Controle de Acesso » Acessos) Portal…](https://ajuda.sankhya.com.br/hc/article_attachments/17263898286615) Para tal, vá até a tela **"Controle de Acessos"** (Caminho de acesso: Configurações » Controle de Acesso » Acessos) Portal de Compras / Vendas (Notas / Pedidos) = Usuário"

![Imagem 2: Para tal, vá até a tela "Controle de Acessos" (Caminho de acesso: Configurações » Controle de Acesso » Acessos) Portal…](https://ajuda.sankhya.com.br/hc/article_attachments/17263869296151)

![Imagem 3: Ainda em Controle de Acessos (Caminho de acesso: Configurações » Controle de Acesso » Acessos) Portal de Compras /…](https://ajuda.sankhya.com.br/hc/article_attachments/17263898294551) Ainda em Controle de Acessos (Caminho de acesso: Configurações » Controle de Acesso » Acessos) Portal de Compras / Vendas (Notas / Pedidos) = Grupo"

![Imagem 4: Ainda em Controle de Acessos (Caminho de acesso: Configurações » Controle de Acesso » Acessos) Portal de Compras /…](https://ajuda.sankhya.com.br/hc/article_attachments/17263869300631)

![Imagem 5: No Portal de compras (Caminho de acesso: Comercial » Consulta » Portal de Compras), clique em "Outras Opções" e depois…](https://ajuda.sankhya.com.br/hc/article_attachments/17263898301463)No **Portal de compras** (Caminho de acesso: Comercial » Consulta » Portal de Compras), clique em **"Outras Opções"** e depois em **"Recalcular PIS/COFINS"**

![Imagem 6: No Portal de compras (Caminho de acesso: Comercial » Consulta » Portal de Compras), clique em "Outras Opções" e depois…](https://ajuda.sankhya.com.br/hc/article_attachments/17263869308567)

![Imagem 7: No Portal de vendas (Caminho de acesso à tela: Comercial » Consulta » Portal de Vendas), clique em "Outras Opções" e…](https://ajuda.sankhya.com.br/hc/article_attachments/17263898304151) No **Portal de vendas** (Caminho de acesso à tela: Comercial » Consulta » Portal de Vendas), clique em **"Outras Opções"** e depois em **"Recalcular PIS/COFINS"**.

![Imagem 8: No Portal de vendas (Caminho de acesso à tela: Comercial » Consulta » Portal de Vendas), clique em "Outras Opções" e…](https://ajuda.sankhya.com.br/hc/article_attachments/17263869313047)

**(1)** Foi criada uma caixa de diálogo de confirmação para mostrar caso existam Documentos (NF-e / NFs-e / CT-e),  com status Enviada, Aguardando autorização, Aprovada, Enviada em Epec e com data de Entrada / saída / negociação / movimento menor que 01/04/2011;  

Foi criado um Pop-up de resumo com duas abas “Processados”, “Não Processados” e no rodapé uma caixa de diálogo “Impedimento encontrado para documento selecionado”, para mostrar os motivos de “Não Processados;

**(2)** Pop-up Processados:

![Imagem 9: (2) Pop-up Processados:](https://ajuda.sankhya.com.br/hc/article_attachments/9682770459287)

**(2)** Pop-up Não processados:

![Imagem 10: (2) Pop-up Não processados:](https://ajuda.sankhya.com.br/hc/article_attachments/9682757660567)

**(1)** Também foi colocado um pop-up com as mensagens abaixo para mostrar quando o usuário clicar na opção Recalcular PIS/COFINS e que na seleção existam documentos na situação: 

“Existem documentos com status **Enviada/Aguardando Autorização/Aprovada/Enviada em Epec,** ou com data de Entrada/Negociação/Movimento, menor que 01/04/2011. Deseja continuar?

NF-e: se atualizada, o XML ficará inconsistente com os novos valores.

NFS-e: se atualizada, não calcula valores retidos.”

![Imagem 11: NFS-e: se atualizada, não calcula valores retidos.”](https://ajuda.sankhya.com.br/hc/article_attachments/9682699754007)

- Não serão alteradas informações nas NOTAS, o recálculo ocorrerá apenas na TGFDIN para PIS/COFINS (codimp = 6 e 7).
- Não Efetuará Recálculo para notas fiscais de Importação CFOP iniciados com 3XXX;
- Não Efetuará Recálculo para notas fiscais de Exportação CFOP iniciados com 7XXX;
- O processo “Recalcular PIS/COFINS” utilizará a rotina de cálculo de PIS/COFINS) do W;
- Somente TOPS com TEM PIS ou TEM COFINS ligado;
- Somente TOPS com ATUALLIVFIS <> 'N' OR TIPMOV IN ('O','C','P','V')  (a mesma utilizada na rotina de cálculo de PIS/COFINS) do W ou seja, com o campo Atualização de Livro ICMS: Diferente de “Não Atualiza” e o campo Tipo de movimento: Igual a: O - Pedido de Compra, C - Compra, P - Pedido de Venda, V - Venda);
- **Somente notas:**
  - Confirmadas;
  - Com STATUSNOTA = 'L - Liberada;
  - Com STATUSNFE IN ('A','E','I','S') A - Aprovada, E- Aguardando Autorização, I - Enviada, S - Enviada Epec;
  - Com (STATUSNFSE IN ('A','E','I') OR STATUSNFE = 'M') e STATUSNFE IS NULL; A - Aprovada, E- Aguardando Autorização, I - Enviada, M - Não é NFe,

**![Imagem 12: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17263869317271) IMPORTANTE:**

- A opção Recalcular PIS/COFINS só estará disponível em outras opções quando um ou mais documentos selecionados no portal estiver dentro das regras de possibilidade de serem recalculados, ou seja, tem de ser uma Nota NF-e ou NFS-e, um CT-e, um Pedido de Compra ou um pedido de venda.
- Caso seja selecionado um documento de devolução ou um documento cancelado, a opção Recalcular PIS/COFINS não estará disponível.
- Caso seja selecionado mais de um documento e pelo menos um deles não esteja na condição de ser alterado, a opção de Recalcular PIS/COFINS não ficará disponível.
- Portanto, para que a opção Recalcular PIS/COFINS esteja disponível, filtre ou selecione somente documentos que atendam as condições de serem recalculados.
- A primeira validação que a rotina faz é filtrar documentos através da query abaixo, sendo que os documentos que não aparecem no resultado desta query não serão considerados para o processamento do recálculo. (Não irão aparecer no popup de resumo de processamento):

“SELECT

     C.NUNOTA

,(CASE

        WHEN (SELECT COUNT(1) FROM  TCBINT I WHERE I.NUNICO = C.NUNOTA AND I.ORIGEM = 'E') > 0 THEN 'S'

        ELSE 'N'

       END) AS CONTABILIZADO

FROM

   TGFCAB C

      INNER JOIN TGFTOP T ON(C.CODTIPOPER = T.CODTIPOPER AND C.DHTIPOPER = T.DHALTER)

      INNER JOIN TGFITE I ON(C.NUNOTA = I.NUNOTA AND (I.CODCFO = T.CODCFO\_ENTRADA OR I.CODCFO = T.CODCFO\_SAIDA  OR I.CODCFO = T.CODCFO\_ENTRADA\_FORA OR I.CODCFO = T.CODCFO\_SAIDA\_FORA))

WHERE

   C.STATUSNOTA = 'L'

   AND (T.TEMPIS = 'S' OR T.TEMCOFINS = 'S')

   AND (T.ATUALLIVFIS <> 'N' OR C.TIPMOV IN ('O','C','P','V'))

   AND I.CODCFO NOT BETWEEN '3000' AND '3999'

   AND I.CODCFO NOT BETWEEN '7000' AND '7999'

   AND I.SEQUENCIA > 0

   /\*${NOTAS}\*/ -- Informar aqui as notas que foram selecionadas para recálculo”

- A segunda validação é filtrar documentos através da query abaixo, estes precisarão de confirmação do usuário para serem processados. Essa validação acontece para identificar se deve mostrar o popup de confirmação ou não, sendo que os documentos que aparecerem nessa query são as notas que precisam da confirmação do usuário, ou seja, o popup de confirmação vai aparecer. As notas que não aparecem nessa query não precisarão da confirmação do usuário.

SELECT NVL(NOTAS.NUNOTA, 0) FROM

(   SELECT NUNOTA FROM TGFCAB

    WHERE STATUSNFE IN ('A','E','I','S')

    AND STATUSNFSE IS NULL

 UNION ALL

    SELECT NUNOTA FROM TGFCAB

    WHERE STATUSNFSE IN ('A','E','I')

    AND STATUSNFE IS NULL 

    OR STATUSNFE = 'M'

UNION ALL

    SELECT NUNOTA FROM TGFCAB

    WHERE STATUSCTE IN ('A','E','I','S')

    AND STATUSNFSE IS NULL

    AND STATUSNFE IS NULL 

    OR STATUSNFE = 'M'

UNION ALL

    SELECT NUNOTA FROM TGFCAB

    WHERE DTENTSAI < '01/04/2011'

    OR DTNEG < '01/04/2011'

    OR DTMOV < '01/04/2011'

) NOTAS

--WHERE    /\*${NOTAS}\*/ -- Informar aqui as notas que foram selecionadas para recálculo.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9682795930775-Recalcular-PIS-COFINS#top)
