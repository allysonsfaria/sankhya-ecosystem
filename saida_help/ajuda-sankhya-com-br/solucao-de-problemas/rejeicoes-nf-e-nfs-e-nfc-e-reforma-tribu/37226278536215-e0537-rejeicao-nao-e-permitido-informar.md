---
id: "37226278536215"
titulo: "E0537 Rejeição: Não é permitido informar benefício municipal (BM deve ser nulo) quando o município de incidência do ISSQN não está \"Ativo\" no Sistema Nacional NFS-e."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226278536215-E0537-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-benef%C3%ADcio-municipal-BM-deve-ser-nulo-quando-o-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN-n%C3%A3o-est%C3%A1-Ativo-no-Sistema-Nacional-NFS-e"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-09-11T14:39:35Z"
rotulos: ["Configuração", "SEFAZ", "Impostos", "Prefeituras", "NFS-e", "Erro", "Artigo atualizado KCS", "Não é permitido informar benefício municipal", "Município de incidência do ISSQN não está \"Ativo\"", "Benefício Municipal", "Benefício fiscal municipal", "Sistema Nacional NFS-e", "Docs Eletrônicos - KCS"]
---

# E0537 Rejeição: Não é permitido informar benefício municipal (BM deve ser nulo) quando o município de incidência do ISSQN não está "Ativo" no Sistema Nacional NFS-e.

**Mensagem**

E0537 Rejeição: Não é permitido informar benefício municipal (BM deve ser nulo) quando o município de incidência do ISSQN não está "Ativo" no Sistema Nacional NFS-e.

**Situação**

Ao tentar emitir uma NFS-e, o sistema apresenta a mensagem de rejeição E0537, indicando que foi informado um **benefício fiscal municipal** para um município que **não está ativo no Sistema Nacional NFS-e**.

**Solução**

**(1)** Confirme o status do município de incidência do ISSQN:

- Verifique se o município informado na nota fiscal está ativo no **Sistema Nacional NFS-e**.
- Para isso, acesse o portal da prefeitura ou consulte a documentação oficial.

**(2)** Caso o município informado na nota não esteja ativo no **Sistema Nacional NFS-e**, siga os passos abaixo para remover o benefício fiscal municipal:

- Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação – TOP).
- Localize o tipo de operação utilizado na emissão da NFS-e.
- Na aba **“NFS-e”**, verifique se há algum **benefício fiscal municipal** configurado.
- Se houver, remova-o, deixando o campo **em branco ou nulo**.

**(3)** Se o município estiver ativo no **Sistema Nacional NFS-e**, mas a rejeição continuar, verifique:

- Se o **código do benefício fiscal** informado está correto;
- Se ele é **válido para o município** em questão.

Para confirmar, consulte o **manual da prefeitura** com os códigos de benefícios aceitos.

**(4)** Após realizar todos os ajustes necessários, emita novamente a NFS-e para validar se a rejeição foi solucionada.

**CAUSA**

A rejeição ocorre porque foi informado um **benefício fiscal municipal** na NFS-e, porém o **município de incidência do ISSQN** não está cadastrado como ativo no Sistema Nacional NFS-e. Segundo as regras de validação da Sefaz, **somente municípios ativos** no sistema podem ter benefícios fiscais municipais informados nas notas fiscais de serviço eletrônicas.
