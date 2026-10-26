---
id: "33877757302167"
titulo: "Arquivo não encontrado - CORE_E05442"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33877757302167-Arquivo-n%C3%A3o-encontrado-CORE-E05442"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:56:44Z"
rotulos: ["Produtos", "Configuração", "Parceiro", "Parceiros", "Serviços", "CORE_E05442", "GUARDAANEXOBD", "erro", "Arquivo não encontrado", "download", "TSIANX", "repositório de arquivos", "Artigo atualizado KCS", "Financeiro - KCS", "Documentos Eletrônicos"]
---

# Arquivo não encontrado - CORE_E05442

**MENSAGEM:**

[CORE\_E05442] Arquivo não encontrado.

**SITUAÇÃO:**

Essa mensagem de erro é apresentada ao tentar realizar o download de um anexo no sistema. O erro ocorre ao clicar em um anexo e o sistema não localizar o arquivo, mesmo que o registro do anexo esteja visível na tela.

**SOLUÇÃO:**

**(1)**  **Identifique onde o anexo foi inserido. O local de armazenamento depende do tipo de tela e da forma de anexação.**

**(1)**  Anexos em telas legadas (botões no cabeçalho das telas):

- São armazenados apenas como referência na tabela ''**TSIANX'';**
- Os arquivos não são salvos no banco, mesmo que o parâmetro ''**GUARDAANEXOBD''** esteja ativo;
- São gravados diretamente no repositório de arquivos do servidor, como: **/home/mgeweb/Sistema/Anexos/NomeTela.**

**Exemplos:** Telas como **"Parceiros"**, **"Produtos"**, **"Serviços"** ou qualquer tela criada no Construtor de Telas.

**(2)**  **Anexos em abas ou campos específicos:**

- São registrados na tabela TSIATA**;**
- O sistema respeita o parâmetro GUARDAANEXOBD:
  - Se ativado, o anexo é salvo diretamente no banco;
  - Se desativado, o anexo é salvo no repositório de arquivos do servidor.

**Exemplos:** **"Central de Compras"**, **"Vendas"**, **"Movimentações Internas"**, aba **"Anexos"** de cadastro de Parceiros, entre outras.

**(3)**  **Acesse o local físico do arquivo:**

**(1)** Após identificar como o anexo foi feito, acesse o caminho correspondente no servidor (por exemplo, via FTP ou diretamente no sistema operacional do servidor de aplicação) e verifique se o arquivo está presente.

**(4)**  **Se o arquivo não estiver presente:**

- É provável que o arquivo tenha sido removido manualmente por erro humano;
- Tenha sido perdido durante migração de servidor ou movimentação de diretórios sem o devido cuidado;
- Tenha sido alterado por rotinas automatizadas de backup ou limpeza;
- Nunca tenha sido salvo corretamente (problemas de permissão ou falha no upload).

**(5)**  **Verifique as configurações do repositório de arquivos:**

**(1)** O caminho físico dos arquivos do **"Repositório de Arquivos"** é definido pelo parâmetro **"FREPBASEFOLDER"**. Se não for possível realizar o download, provavelmente o caminho foi alterado. Utilize a consulta abaixo para verificar alterações recentes e identificar o responsável:

```
SELECT * FROM TSIPARLGT WHERE CHAVE LIKE '%FREPBASEFOLDER%' ORDER BY DHACAO DESC;
```

**(1)** Caso haja alteração, acesse a pasta original do repositório, recupere os arquivos e inclua-os na pasta atual do repositório.

**Todos os anexos são salvos seguindo a lógica:**

```
/Sistema/Anexos/$INSTANCIA
```

**Exemplos:**

```
/Sistema/Anexos/Parceiro
/Sistema/Anexos/Contrato
/Sistema/Anexos/Produto
```

**Os arquivos são salvos com um hash no nome e sem extensão, por exemplo:**

```
069da704e5a726366961211cc2c2f6e7
0a24f11577a1209b82fff86125d11bf7
0c8fe173bf678bebbc469c6432bcb2a4
```

**Observação:** Os arquivos devem ser salvos no repositório atual sem modificar nada. Qualquer alteração pode causar a perda do vínculo no sistema.

**CAUSA:**

Essa falha está geralmente relacionada a um ou mais dos seguintes fatores:

- O arquivo foi removido fisicamente do diretório onde deveria estar armazenado no servidor;
- O anexo está apenas com o registro de referência na base (TSIANX ou TSIATA), mas o conteúdo real não existe mais;
- Ocorreram alterações na estrutura de diretórios, renomeações de pastas ou migração de servidores, e os arquivos não foram movidos corretamente;
- O parâmetro GUARDAANEXOBD não está respeitado (em casos onde deveria estar ligado para salvar no banco), ou o anexo foi salvo de forma mista (alguns no repositório e outros no banco);
- A tela utilizada para anexar o arquivo influencia diretamente na lógica de armazenamento do anexo, o que pode dificultar a localização do arquivo.
