---
id: "39661254280215"
titulo: "Registro de NFS-e Tomada no Padrão Nacional "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39661254280215-Registro-de-NFS-e-Tomada-no-Padr%C3%A3o-Nacional"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Emissões em conformidade com o Padrão Nacional"
atualizado_em: "2026-09-09T15:29:25Z"
rotulos: ["Configuração", "Fiscal", "Prefeituras", "NFS-e", "Padrão Nacional", "Documentos Eletrônicos"]
---

# Registro de NFS-e Tomada no Padrão Nacional 

**Caminho de Acesso:** Menu Principal > Comercial > Consulta > [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras)

---

#### Descrição da Funcionalidade

Este artigo orienta sobre como registrar Notas Fiscais de Serviço Eletrônicas (NFS-e) emitidas por fornecedores que já utilizam o Padrão Nacional. Com a adoção deste novo modelo por diversos municípios, as séries das notas fiscais passaram a ter até 5 dígitos.

Para garantir que a sua empresa registre esses documentos corretamente, o sistema Sankhya foi atualizado, flexibilizando a digitação na Central de Compras e assegurando a integridade da escrituração fiscal e contábil.

#### Jornada de Uso

**Lançamento na Central de Compras**

Ao receber uma NFS-e do seu fornecedor (serviço tomado) gerada no Padrão Nacional, acesse a [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras) para realizar a entrada do documento.

- No cabeçalho da nota, localize o campo **"Série NFS-e"**.
- Este campo está totalmente liberado para edição e permite a digitação livre de até **5 caracteres** (ex: 12345).
- O sistema aceitará a informação perfeitamente, eliminando antigos bloqueios que limitavam a série a apenas 3 dígitos.

**Escrituração Fiscal e Contábil**

Você não precisa realizar nenhuma configuração adicional para que essa série estendida vá para os seus livros. O sistema fará isso de forma automática:

- Ao salvar a nota, a série informada (com até 5 posições) é armazenada de forma íntegra no banco de dados, sem cortes ou arredondamentos.
- Nos **Livros Fiscais** (Livro de ISS), a série completa do documento será apresentada corretamente.
- Na geração das obrigações acessórias, como o **SPED (EFD Contribuições)**, o sistema levará a série da nota de forma exata para o **Registro A100** (Bloco A), garantindo que o seu arquivo seja validado sem erros pela Receita Federal. O mesmo ocorre para a geração da ECD e ECF.

#### Pontos de Atenção

- **Flexibilidade Estrutural:** embora o Padrão Nacional exija 5 posições para a série, o banco de dados do sistema foi estruturado para aceitar até 20 caracteres. Isso evita que a sua operação seja interrompida caso alguma prefeitura adote layouts maiores no futuro.
- **Compatibilidade:** o comportamento para o lançamento de notas de fornecedores antigos ou de municípios que ainda utilizam séries curtas (de 1 a 3 dígitos) permanece inalterado. O sistema aceitará essas notas normalmente.

#### FAQ – Dúvidas Frequentes

**Meu fornecedor não usa o Padrão Nacional e a série da nota dele tem apenas 2 dígitos. O que eu faço?** Siga o processo normalmente. O sistema mantém total compatibilidade com notas que possuem séries de 1 a 3 posições. Basta digitar a série correspondente e confirmar a nota.

**O sistema vai cortar ou abreviar a série se eu digitar 5 números?** Não. A série será persistida e armazenada integralmente. Se você digitar "12345", é exatamente essa numeração que aparecerá nos seus Livros Fiscais e no arquivo do SPED.

**Preciso ativar algum parâmetro para liberar a digitação de 5 dígitos na Central de Compras?** Não é necessário. A flexibilização do campo "Série NFS-e" na Central de Compras é nativa e já está disponível para uso sem a necessidade de ligar parâmetros adicionais.
