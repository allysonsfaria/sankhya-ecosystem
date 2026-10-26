---
id: "37225632575383"
titulo: "E0458 Rejeição: Uma NFS-e cancelada não pode ser informada para dedução/redução"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225632575383-E0458-Rejei%C3%A7%C3%A3o-Uma-NFS-e-cancelada-n%C3%A3o-pode-ser-informada-para-dedu%C3%A7%C3%A3o-redu%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:50Z"
rotulos: ["ISS", "Configuração", "Prefeituras", "NFS-e", "Erro", "Nota Fiscal de Serviço Eletrônica (NFS-e)", "NFS-e cancelada não pode ser informada para dedução/redução", "Notas canceladas não possuem validade fiscal", "NFS-e previamente cancelada", "Dedução ou redução da base de cálculo do ISS", "dedução ou redução na base de cálculo do ISS", "Rejeição E0458", "E0458 Rejeição"]
---

# E0458 Rejeição: Uma NFS-e cancelada não pode ser informada para dedução/redução

**MENSAGEM**

E0458 Rejeição: Uma NFS-e cancelada não pode ser informada para dedução/redução.

**SITUAÇÃO**

Ao emitir uma **Nota Fiscal de Serviço Eletrônica (NFS-e)**, o usuário tentou informar uma **NFS-e previamente cancelada** como base para **dedução ou redução** na base de cálculo do ISS. O sistema da prefeitura rejeitou a operação, pois **notas canceladas não possuem validade fiscal** e não podem ser utilizadas para fins de dedução tributária.

**SOLUÇÃO**

**(1)** Acesse a tela [**''Portal de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consulta » Portal de Vendas) e localize a NFS-e informada para dedução.

- Confirme se a nota está realmente **cancelada**.

**(2)** Se a nota estiver **cancelada indevidamente**, consulte o **setor fiscal da prefeitura** para verificar se é possível reverter o cancelamento ou se é necessário emitir uma **nota substituta**.

**(3)** Se o cancelamento foi correto, **remova a referência** à NFS-e cancelada no campo de dedução/redução da nova nota que está sendo emitida.

**(4)** Informe apenas NFS-e **válidas e não canceladas** para fins de dedução ou redução na base de cálculo do ISS. Certifique-se de que a nota referenciada possua status **"Aprovada"** ou equivalente.

**(5)** Se for necessário utilizar uma **nota substituta**, acesse a tela [**''Cidades''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades), na aba **"NFS-e"**, e verifique se a prefeitura permite a substituição via **webservice**.

**(6)** Após realizar os ajustes necessários, **reenvie a NFS-e** com as informações corretas de dedução/redução.

**CAUSA**

A rejeição ocorre porque o sistema da prefeitura **não permite que NFS-e canceladas** sejam utilizadas como referência para **dedução ou redução da base de cálculo do ISS**. Notas canceladas **perdem sua validade fiscal** e não podem ser consideradas em operações tributárias. O usuário tentou vincular uma nota com **status "Cancelada"** no campo de dedução, violando as **regras de validação da administração tributária municipal**.
