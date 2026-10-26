---
id: "35270029343127"
titulo: "CORE_E02616: TOP não pode ser 'NF-e' e 'NFS-e' ao mesmo tempo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35270029343127-CORE-E02616-TOP-n%C3%A3o-pode-ser-NF-e-e-NFS-e-ao-mesmo-tempo"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:25:41Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "TOP", "NFS-e", "NF-e e NFS-e", "Erro", "'NF-e' e 'NFS-e'", "CORE_E02616", "'NF-e' e 'NFS-e' ao mesmo tempo", "TOP não pode ser 'NF-e' e 'NFS-e' ao mesmo tempo"]
---

# CORE_E02616: TOP não pode ser 'NF-e' e 'NFS-e' ao mesmo tempo

**MENSAGEM**

[CORE\_E02616] TOP não pode ser 'NF-e' e 'NFS-e' ao mesmo tempo.

**SITUAÇÃO**

A mensagem aparece quando o usuário tenta configurar uma **"TOP"** (Configurações » Fiscal » TOP) com os campos **"NF-e"** e **"NFS-e"** habilitados simultaneamente. O sistema identifica este conflito durante a validação e impede o salvamento da configuração.

**SOLUÇÃO**

#### Configure o campo NFS-e:

**(1)** Acesse a tela **"TOP"** (Configurações » Fiscal » TOP) e localize a TOP que apresentou o erro.

**(2)** Clique na aba **"NFS-e"** da TOP.

**(3)** No campo **"NFS-e"**, selecione a opção **"Convencional (Não usa NFS-e)"** e salve a alteração.

#### Configure o campo NF-e:

**(4)**  Em seguida, ainda TOP que apresentou o erro, acesse a aba **"NF-e/NFC-e/CF-e".**

**(5)** Configure o campo **"NF-e"** conforme desejado (Normal, Complementar, Anulação ou Devolução) e salve.

**(6)** **Importante:** **sempre configure primeiro o campo NFS-e como "Convencional" antes de alterar o campo NF-e para evitar este erro de validação.**

#### Observações:

**Quando há uma configuração legada,** na qual não existe licença de emissão de NFS-e, o campo NFS-e pode ficar com valor padrão e não permitir alteração através da interface. Nestes casos:

- O valor do campo NFS-e no banco de dados pode estar diferente de "M" (Convencional)
- É necessário que seu DBA execute um comando SQL para alterar o valor para (M - Convencional)

Após a alteração pelo DBA, será possível configurar o campo NF-e normalmente

**CAUSA**

O erro ocorre porque o sistema não permite que uma TOP seja configurada para emitir **NF-e** (Nota Fiscal Eletrônica) e **NFS-e** (Nota Fiscal de Serviços Eletrônica) simultaneamente. A validação identifica quando o campo **"NF-e"** está configurado com valores diferentes de "Não emite" enquanto o campo **"NFS-e"** não está como "Convencional (Não usa NFS-e)".
