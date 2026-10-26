---
id: "8425198187671"
titulo: "Código de tributação não permite incidência do ISSQN fora deste município"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/8425198187671-C%C3%B3digo-de-tributa%C3%A7%C3%A3o-n%C3%A3o-permite-incid%C3%AAncia-do-ISSQN-fora-deste-munic%C3%ADpio"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:12:02Z"
rotulos: ["Cidades", "XML", "Impostos", "não apagar", "E240", "Prefeituras", "NFS-e", "Restrição de Incidência do ISSQN", "Código de tributação", "ISSQN"]
---

# Código de tributação não permite incidência do ISSQN fora deste município

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18977775772439) MENSAGEM**:

[E240] Código de tributação não permite incidência do ISSQN fora deste município.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18977775778071) SITUAÇÃO:**

Ao emitir uma NFS-e a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18977775781399) CAUSA:**

Cidade de Prestação de Serviço incorreta ou não informada. Ou a Prefeitura não permite retenção de ISS.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18977775787671) SOLUÇÃO:**

Verifique o seguinte passo a passo:

- Exporte o arquivo XML no Portal de Vendas (Caminho de acesso: NFS-e > Gerar XML do RPS para NFS-e) e verifique como está a tag ISSRetido.
- Se a tag estiver preenchida com '2', existe a retenção de ISS. Caso realmente haja a retenção, verifique se foi informado corretamente a Cidade de Prestação de Serviço na Central de Vendas.
- Se o erro persistir, mesmo com os passos anteriores verificados, valide no manual da Prefeitura do Município se é permitido a retenção para o determinado serviço.
