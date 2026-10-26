---
id: "8338467554199"
titulo: "Apenas empresas inscritas neste município podem efetuar retenção de ISSQN"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/8338467554199-Apenas-empresas-inscritas-neste-munic%C3%ADpio-podem-efetuar-reten%C3%A7%C3%A3o-de-ISSQN"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:12:12Z"
rotulos: ["Configuração", "Parceiro", "TOP", "não apagar", "E039", "Prefeituras", "NFS-e", "ISSQN", "Problema na retenção de ISS", "Emissão de NFS-e", "Ajustes necessários"]
---

# Apenas empresas inscritas neste município podem efetuar retenção de ISSQN

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16593740574871) MENSAGEM:**

E039: Apenas empresas inscritas neste município podem efetuar retenção de ISSQN.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16593732559127) SITUAÇÃO:**

Ao tentar emitir nota fiscal para fora do município, com parceiros que retém ISS, a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16593740579991)SOLUÇÃO:**

O tomador do serviço não foi encontrado na base de dados do município, não sendo permitida a retenção. Acerte o CNPJ e/ou Inscrição Municipal ou altere o campo ISSQN Retido para 2 (Sem retenção de ISSQN). No exemplo abaixo no cadastro do parceiro, estava marcado para reter ISS, então foi alterado para não reter.

![Imagem 4: O tomador do serviço não foi encontrado na base de dados do município, não sendo permitida a retenção. Acerte o CNPJ…](https://ajuda.sankhya.com.br/hc/article_attachments/16593732567063)

Compare o XML da NFS-e emitida na prefeitura com a NFS-e emitida no sistema.

Verifique se foi preenchido o campo **"Cidade"** no rodapé da nota (neste deve ser informada a cidade onde ocorreu a prestação do serviço), caso não tenha sido, faça o devido preenchimento.

Referente a primeira situação: **TAG NaturezaOperacao>2</NaturezaOperacao>**
Essa informação é configurada no sistema no cadastro da **TOP** (Caminho de acesso à tela: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), na aba NFS-e campo: Cód. Natureza Oper. ISS (NFS-e).

![Imagem 5: Referente a primeira situação: TAG NaturezaOperacao>2</NaturezaOperacao> Essa informação é configurada no sistema no…](https://ajuda.sankhya.com.br/hc/article_attachments/16593732569239)

Alterado esse campo para que seja destacado no XML a opção 2, assim como  consta no arquivo XML gerado pelo site da NF-e aprovada na Prefeitura, e verificando nas preferências da empresa se está configurado o ambiente de produção para emissão de NFS-e, a nota será aprovada com sucesso.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16593740590359)CAUSA:**

Emitir nota fora do município para parceiros que retém ISS e as configurações estejam incorretas.
