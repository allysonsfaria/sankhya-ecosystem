---
id: "360044350313"
titulo: "Como personalizar criando um campo UF no cadastro de Parceiro?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044350313-Como-personalizar-criando-um-campo-UF-no-cadastro-de-Parceiro"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:58:06Z"
rotulos: ["#criadoRoger", "Configuração", "Parceiro", "Cidades", "Dicionário de Dados", "Personalização", "Personalização: Campo UF em Parceiro"]
---

# Como personalizar criando um campo UF no cadastro de Parceiro?

![Imagem 1: Acesse a tela " Dicionário de Dados" (Caminho de acesso: Configurações » Avançado » Dicionário de Dados), em filtros…](https://ajuda.sankhya.com.br/hc/article_attachments/16974796069271)  Acesse a tela **"Dicionário de Dados"** (Caminho de acesso: Configurações » Avançado » Dicionário de Dados), em filtros rápidos, no campo **"Nome de tabela"** digite: TGFPAR e clique em **"Aplicar"**:

![Imagem 2: Acesse a tela " Dicionário de Dados" (Caminho de acesso: Configurações » Avançado » Dicionário de Dados), em filtros…](https://ajuda.sankhya.com.br/hc/article_attachments/13641304691351)

1.1- Na Aba **"Campos"**, clique em Novo [+]

- Nome do Campo: UF
- Descrição do campo: UF
- Tipo de dados: Texto
- Apresentação: Padrão
- Marcar: 'Visível no Grid de pesquisa' e também 'Campo calculado'

**Expressão [Oracle]:**

String uf = "";
$sql.setParam("CODCID", $col\_CODCID);
$sql.select("UFS.UF || '-' || UFS.DESCRICAO", "TSIUFS UFS INNER JOIN TSICID CID ON CID.UF = UFS.codUF", "cid.codcid = {CODCID}");
if($sql.next()) {
uf = $sql.getString(1);
}
return uf;

**Expressão [SQL]:**

String uf = "";
$sql.setParam("CODCID", $col\_CODCID);
$sql.select("UFS.UF + '-' + UFS.DESCRICAO", "TSIUFS UFS INNER JOIN TSICID CID ON CID.UF = UFS.codUF", "cid.codcid = {CODCID}");
if($sql.next()) { uf = $sql.getString(1); }
return uf;

![Imagem 3: String uf = ""; $sql.setParam("CODCID", $col_CODCID); $sql.select("UFS.UF + '-' + UFS.DESCRICAO", "TSIUFS UFS INNER…](https://ajuda.sankhya.com.br/hc/article_attachments/13641310552855)

1.2 Salve

1.3 Clique em **"Outras Opções"** e em **"Reiniciar esta Unidade de Dados".**

![Imagem 4: Acesse a tela " Parceiros" (Caminho de acesso: Configurações » Cadastros » Parceiros). Vale destacar que se esta tela…](https://ajuda.sankhya.com.br/hc/article_attachments/16974780833047) Acesse a tela **"Parceiros"** (Caminho de acesso: Configurações » Cadastros » Parceiros). Vale destacar que se esta tela já estiver aberta, feche-a e abra novamente

2.1 Clique no botão **"Configuração da Tela"**

- Busque pelo campo **"UF"** em **"Campos Disponíveis"**, que deverá aparecer logo abaixo;
- Clique no campo UF;
- Na Aba **"Campos selecionados"**, clique na aba **"Endereço"**
- Clique no botão **"Adicionar Campo"** para que seja adicionado o campo UF, selecionado anteriormente.
- Posicione o campo UF logo abaixo do campo **"Cód. Cidade"**
- Clique no botão salvar

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16974796075031) OBSERVAÇÃO:**

Lembrando que esta opção é uma personalização, que deve ser criada pela empresa de acordo com sua necessidade e é de inteira responsabilidade dos mesmos.
