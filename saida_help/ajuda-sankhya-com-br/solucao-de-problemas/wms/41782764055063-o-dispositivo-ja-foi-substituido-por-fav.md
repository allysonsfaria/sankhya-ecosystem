---
id: "41782764055063"
titulo: "O dispositivo ' ' já foi substituido, por favor escolher outro para realizar a troca. Data para realizar a próxima troca XX/XX/XXXX. Código: SVC_E00916'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41782764055063-O-dispositivo-j%C3%A1-foi-substituido-por-favor-escolher-outro-para-realizar-a-troca-Data-para-realizar-a-pr%C3%B3xima-troca-XX-XX-XXXX-C%C3%B3digo-SVC-E00916"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-08-13T12:04:24Z"
rotulos: ["Configuração", "WMS", "Erro", "Coletor WMS TotalCross", "Coletor WMS", "Squad WMS", "WMS - KCS", "PERMSUBSTDISP", "TotalCross"]
---

# O dispositivo ' ' já foi substituido, por favor escolher outro para realizar a troca. Data para realizar a próxima troca XX/XX/XXXX. Código: SVC_E00916'

**MENSAGEM**

O dispositivo ' ' já foi substituido, por favor escolher outro para realizar a troca. Data para realizar a próxima troca XX/XX/XXXX. Código: SVC\_E00916'

**SITUAÇÃO**

Ao tentar substituir o registro de licença do Coletor WMS TotalCross, por meio da tela **''Administração de Licença''** (Contratos e Serviços » Administração de licença) , na aba **''Solicitações Pendentes''**, utilizando o botão **''Substituir Dispositivo''**, foi selecionado um dispositivo cuja licença havia sido liberada há menos de 30 dias corridos.

**SOLUÇÃO**

**(1)** Ative o parâmetro **''PERMSUBSTDISP''** - **"Permite substituir dispositivos com menos de 30 dias"**.

**(2)** Após a ativação, será possível realizar a substituição do dispositivo mesmo que o período mínimo de 30 dias ainda não tenha sido atingido.

**CAUSA**

Trata-se de comportamento sistêmico, pois, nativamente foi criado o produto, para ser possível substituir o uso da licença, somente 30 dias após a liberação do dispositivo.
