---
id: "9625908732055"
titulo: "O tomador contém um endereço com Cidade não identificada e sem o país informado, caso esteja emitindo uma nota fiscal para tomador do exterior informe o país do mesmo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9625908732055-O-tomador-cont%C3%A9m-um-endere%C3%A7o-com-Cidade-n%C3%A3o-identificada-e-sem-o-pa%C3%ADs-informado-caso-esteja-emitindo-uma-nota-fiscal-para-tomador-do-exterior-informe-o-pa%C3%ADs-do-mesmo"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:07:11Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "Cidades", "não apagar", "CORE_E06044", "NFS-e", "Erro de Cadastro de Cidade na Emissão de NFS-e", "Erro", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# O tomador contém um endereço com Cidade não identificada e sem o país informado, caso esteja emitindo uma nota fiscal para tomador do exterior informe o país do mesmo

**Mensagem**

[CORE\_E06044] O tomador contém um endereço com cidade não identificada e sem o país informado, caso esteja emitindo uma nota fiscal para tomador do exterior informe o país do mesmo. Erro na validação do nome da cidade cadastrada no sistema emissor de nota fiscal, que difere do nome oficial registrado na base de dados do IBGE (Instituto Brasileiro de Geografia e Estatística).

**Situação**

Ao tentar faturar a **"Nota Fiscal Eletrônica de Serviços (NFS-e)"**, o sistema apresenta erro relacionado ao cadastro de endereço do cliente ou do prestador de serviços. A mensagem indica que a cidade não está identificada ou que há divergência entre o nome cadastrado e o nome oficial do município na tabela do IBGE. Este erro impede a autorização e transmissão da nota fiscal para a prefeitura.

**Causa**

O erro ocorre quando o nome da cidade cadastrado no sistema emissor de nota fiscal está diferente do nome oficial registrado na base de dados do IBGE. Esta divergência pode acontecer por:

- Erros de digitação no cadastro do parceiro ou da cidade;
- Uso de abreviações não oficiais do nome do município;
- Diferenças de acentuação ou caracteres especiais;
- Cadastros antigos que não foram atualizados conforme o padrão do IBGE;
- Ausência de informações obrigatórias como o país no endereço.

**Solução**

Para resolver o problema, corrija o cadastro da cidade no sistema seguindo os passos abaixo:

**(1)** Acesse a tela **"Cidades"** (Configurações >> Cadastros >> Endereços >> Cidades) e localize a cidade para a qual está emitindo a nota, ou acesse a tela **"Parceiros"** (Configurações >> Cadastros >> Parceiros) caso precise ajustar o endereço específico do cadastro.

**(2)** Verifique se o nome da cidade está exatamente igual ao informado no site do IBGE, respeitando acentuação, espaços e caracteres especiais.

**(3)** Consulte o nome oficial do município no site oficial do IBGE: [Brasil | Cidades e Estados | IBGE](https://www.ibge.gov.br/cidades-e-estados).

**(4)** Realize a correção do nome do cadastro da cidade conforme o padrão oficial e salve as alterações.

**(6)** Tente gerar o lote da **"NFS-e"** novamente.

**Exemplos visuais:**

![Imagem 1: Exemplos visuais:](https://ajuda.sankhya.com.br/hc/article_attachments/18667165073943)

![Imagem 2: Exemplos visuais:](https://ajuda.sankhya.com.br/hc/article_attachments/18667165085591)

**Observação:** Caso o erro persista, verifique também se o campo **"País"** está devidamente preenchido no endereço do parceiro, pois a ausência desta informação também pode gerar rejeições.
