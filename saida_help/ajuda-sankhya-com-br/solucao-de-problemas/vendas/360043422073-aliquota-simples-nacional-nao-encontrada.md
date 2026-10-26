---
id: "360043422073"
titulo: "Alíquota Simples Nacional não encontrada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043422073-Al%C3%ADquota-Simples-Nacional-n%C3%A3o-encontrada"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:55Z"
rotulos: ["#PUBLIFER", "CORE_E04495", "Alíquotas", "Configuração", "NF-e", "Central de Vendas", "Simples Nacional", "Impostos", "Simples Nacional alíquota faltante", "Ajustar preferências empresa", "Verificar partilha configurada"]
---

# Alíquota Simples Nacional não encontrada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16118205126039) MENSAGEM:**

[CORE\_E04495] Alíquota Simples Nacional não encontrada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16118205132823) SOLUÇÃO:**

Na Central de Vendas, ao realizar a emissão da NF-e, o sistema verifica se a empresa é Optante pelo Simples Nacional e em caso afirmativo, efetua as seguintes análises:

![Imagem 3: Sendo um lançamento de produtos, de origem estrangeira (Cadastro de Produtos, aba Geral, campo Origem do produto: 1 ou…](https://ajuda.sankhya.com.br/hc/article_attachments/16118205136919) Sendo um lançamento de produtos, de origem estrangeira (Cadastro de Produtos, aba Geral, campo Origem do produto: 1 ou 6) ou de fabricação própria (Cadastro de Produtos, aba Geral, campo Usado como: Venda (Fabricação Própria)), será feita a busca nas **"[Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)"**, do **Tipo de Partilha vigente igual a Indústria** para se calcular o ICMS e IPI.

![Imagem 4: Para demais produtos, o sistema irá buscar o Tipo de Partilha vigente igual a Comércio para calcular o ICMS e IPI;](https://ajuda.sankhya.com.br/hc/article_attachments/16118225543703) Para demais produtos, o sistema irá buscar o **Tipo de Partilha vigente igual a Comércio**para calcular o ICMS e IPI;

![Imagem 5: Para Serviços, o sistema irá buscar o Tipo de Partilha informado na aba "Configurações por Empresa" ; não encontrando…](https://ajuda.sankhya.com.br/hc/article_attachments/16118205146647) Para Serviços, o sistema irá buscar o Tipo de Partilha informado na aba **"Configurações por Empresa"**; não encontrando ou se estiver em branco, irá buscar na aba **"Impostos"**. Se estes dois campos estiverem em branco, o sistema irá tratar o Simples Nacional aplicando a regra já existente.

![Imagem 6: Para Serviços, o sistema irá buscar o Tipo de Partilha informado na aba "Configurações por Empresa" ; não encontrando…](https://ajuda.sankhya.com.br/hc/article_attachments/14611140153111)

Dessa forma, diante do cenário acima, atente-se as configurações abaixo:

![Imagem 7: Na tela Partilha/Anexo do Simples Nacional, uma partilha devidamente configurada:](https://ajuda.sankhya.com.br/hc/article_attachments/16118225554839) Na tela Partilha/Anexo do Simples Nacional, uma partilha devidamente configurada:

**(2)** Se conforme item 1, partilha de INDÚSTRIA;

**(2)** Se conforme item 2, partilha de COMÉRCIO;

![Imagem 8: (2) Se conforme item 2, partilha de COMÉRCIO;](https://ajuda.sankhya.com.br/hc/article_attachments/12097454504087)

![Imagem 9: Nas Preferências da Empresa (Comercial » Preferências » Empresa) o número único de partilha vinculado na aba "Simples…](https://ajuda.sankhya.com.br/hc/article_attachments/16118225563543) Nas Preferências da Empresa (Comercial » Preferências » Empresa) o número único de partilha vinculado na aba **"Simples Nacional"**.

![Imagem 10: Nas Preferências da Empresa (Comercial » Preferências » Empresa) o número único de partilha vinculado na aba "Simples…](https://ajuda.sankhya.com.br/hc/article_attachments/14611145346455)

![Imagem 11: Caso trabalhe com Partilhas diferenciadas por produto, verifique a configuração do campo abaixo na tela de " Cadastro…](https://ajuda.sankhya.com.br/hc/article_attachments/16118205162135) Caso trabalhe com Partilhas diferenciadas por produto, verifique a configuração do campo abaixo na tela de **"[Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)"**:

![Imagem 12: Caso trabalhe com Partilhas diferenciadas por produto, verifique a configuração do campo abaixo na tela de " Cadastro…](https://ajuda.sankhya.com.br/hc/article_attachments/14611145448983)

**![Imagem 13: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16118205166615) OBSERVAÇÃO:**

Considere desligar o parâmetro **VALPARTSNUNICA - Valida partilha do Simples Nac. mesmo sendo única?**, caso a empresa não trabalhe com mais de uma partilha.

**![Imagem 14: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16118205169431) CAUSA:**

Ao realizar emissão de NF-e/NFS-e através do sistema, sendo a empresa emitente optante pelo Simples Nacional, se não localizada a partilha para cálculo de impostos, será retornada a mensagem.
