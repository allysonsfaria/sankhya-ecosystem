---
id: "36670952315543"
titulo: "Por que o evento S-2230 das férias não está sendo gerado?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36670952315543-Por-que-o-evento-S-2230-das-f%C3%A9rias-n%C3%A3o-est%C3%A1-sendo-gerado"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:28:15Z"
rotulos: ["Configuração", "Eventos", "eSocial", "Folha de Pagamento", "S-2230", "S-2230 das férias", "Central de Projetos"]
---

# Por que o evento S-2230 das férias não está sendo gerado?

O evento **S-2230** é responsável por registrar afastamentos, como férias, no eSocial.

No entanto, em algumas situações, o sistema **não gera esse evento imediatamente**, o que pode causar dúvidas no acompanhamento dos envios.

Isso ocorre devido a uma **regra de prazo utilizada pelo próprio sistema** para definir quais ocorrências devem ser consideradas no envio ao eSocial.

### Como funciona essa regra?

O sistema só considera **ocorrências cuja data final esteja dentro de um período de até 60 dias** contados a partir da data atual.

Exemplo:

Se **hoje é 19/11/2025**:

- Somando 60 dias, o sistema chega ao dia **17/01/2026**.
- Portanto:

  - **Ocorrências com data final até 17/01/2026** → serão consideradas e podem gerar o evento S-2230.
  - **Ocorrências com data final após 17/01/2026** → ainda **não entram** no envio.

### Quando o evento será gerado?

Assim que a **data final das férias** entrar dentro do intervalo de **60 dias** em relação à data atual, o sistema passa a considerar a ocorrência, e o **evento S-2230 será gerado normalmente**.
