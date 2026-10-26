---
id: "37222832317463"
titulo: "E0231 Rejeição: IM do emitente tomador não está autorizado a emitir NFS-e, conforme informações complementares registradas no CNC NFS-e do município emissor informado na DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222832317463-E0231-Rejei%C3%A7%C3%A3o-IM-do-emitente-tomador-n%C3%A3o-est%C3%A1-autorizado-a-emitir-NFS-e-conforme-informa%C3%A7%C3%B5es-complementares-registradas-no-CNC-NFS-e-do-munic%C3%ADpio-emissor-informado-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:23Z"
rotulos: ["Configuração", "Prefeituras", "NFS-e", "Passos para resolver", "Erro", "Como Resolver", "Inscrição Municipal (IM)", "Prefeitura do município emissor", "CNC NFS-e (Cadastro Nacional Centralizado de Notas Fiscais de Serviços Eletrônicas)", "Administração Tributária Municipal", "IM"]
---

# E0231 Rejeição: IM do emitente tomador não está autorizado a emitir NFS-e, conforme informações complementares registradas no CNC NFS-e do município emissor informado na DPS.

**MENSAGEM**

E0231 Rejeição: IM do emitente tomador não está autorizado a emitir NFS-e, conforme informações complementares registradas no CNC NFS-e do município emissor informado na DPS.

**SITUAÇÃO**

Ao tentar emitir uma NFS-e, o usuário recebe a rejeição E0231 informando que a **Inscrição Municipal (IM)** do emitente ou tomador **não está autorizada** a emitir notas fiscais de serviço eletrônicas no município.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas) e localize o cadastro da empresa emitente da NFS-e.

**(2)** Na aba **"Geral"**, verifique se o campo **"Inscrição Municipal"** está preenchido corretamente, **sem caracteres especiais** (pontos, traços ou barras), apenas números.

**(3)** Compare a Inscrição Municipal cadastrada no sistema com o **documento oficial fornecido pela Prefeitura** que valida o cadastro da empresa para emissão de NFS-e:

- Certifique-se de que **todos os dígitos estão corretos**, incluindo zeros à esquerda, se houver;
- Verifique se não há **dígitos faltando ou excedentes**.

**(4)** Caso a empresa seja **tomadora do serviço**, acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do parceiro tomador.

**(5)** Na aba **"Identificação"**, verifique se o campo **"Inscrição Municipal"** do tomador está preenchido corretamente, seguindo as mesmas orientações do passo 3.

**(6)** Após corrigir as informações cadastrais, **salve as alterações** realizadas.

**(7)** Caso a empresa ainda não esteja autorizada junto à Prefeitura, **solicite a autorização** para emissão de NFS-e diretamente no portal da Prefeitura do município emissor.

**(8)** Após a confirmação da autorização pela Prefeitura e a correção dos dados cadastrais, **gere novamente o lote da NFS-e**.

**CAUSA**

Esta rejeição ocorre quando a **Inscrição Municipal cadastrada no sistema Sankhya** está divergente das informações registradas no **Cadastro Nacional de Contribuintes (CNC) da NFS-e** junto à Prefeitura do município emissor. Outra causa comum é quando o contribuinte **não está devidamente autorizado** pela Administração Tributária Municipal para emitir notas fiscais de serviço eletrônicas, seja por pendências cadastrais, documentação incompleta ou falta de solicitação formal de credenciamento junto ao município.
