---
id: "39355003451031"
titulo: "LIV_E00495 - Já foi inserido pela Configuração de Ajustes de Apuração número <codcfg-existente>, e  você está tentando inserir novamente utilizando a configuração <codcfg-atual>"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39355003451031-LIV-E00495-J%C3%A1-foi-inserido-pela-Configura%C3%A7%C3%A3o-de-Ajustes-de-Apura%C3%A7%C3%A3o-n%C3%BAmero-codcfg-existente-e-voc%C3%AA-est%C3%A1-tentando-inserir-novamente-utilizando-a-configura%C3%A7%C3%A3o-codcfg-atual"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-09-02T14:17:32Z"
rotulos: ["Configuração", "Fiscal", "Impostos", "EFD", "ICMS/IPI", "Erro", "Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# LIV_E00495 - Já foi inserido pela Configuração de Ajustes de Apuração número <codcfg-existente>, e  você está tentando inserir novamente utilizando a configuração <codcfg-atual>

Compreenda que você está enfrentando um erro relacionado à geração dos registros C195/C197 no EFD ICMS/IPI, onde o sistema indica que um ajuste já foi inserido pela configuração número 26 e está sendo tentado inserir novamente pela configuração 60.

### Mensagem

O ajuste referente à nota:

NUNOTA: <nunota>
SEQUENCIA: <sequencia>

Já foi inserido pela Configuração de Ajustes de Apuração número <codcfg-existente>, e  você está tentando inserir novamente utilizando a configuração <codcfg-atual>.

### Situação

Este erro ocorre durante a geração dos livros fiscais (Livros Fiscais >> arquivos>> Geração ICMS/IPI) quando o campo "Gerar Ajustes" está com alguma marcação para atualizar os ajustes e, temos configurações liberadas, na tela (Livros Fiscais >> arquivos>> Configurações de Ajustes de Apuração)

A mensagem aparece quando duas configurações geram, para o mesmo item da nota, um ajuste que o sistema entende como o mesmo lançamento — mesma nota, mesmo item, mesma empresa,  mesmo Cód. de Ajuste. É a trava que impede o mesmo ajuste de ser contado duas vezes na apuração e sair em duplicidade no SPED Fiscal.

Quando a configuração tem origem no financeiro, a mensagem traz NUFIN no lugar de NUNOTA.

### Solução

**(1)** **Compare as configurações citadas.** Na rotina Configuração de Ajustes de Apuração, abra as duas pelos números da mensagem e compare **Cód. de Ajuste** e **Observação padrão**. Coincidindo os dois, o conflito está identificado — e essa comparação não depende do livro.

**(2)** Deveriam ser ajustes distintos → diferencie o Cód. de Ajuste em uma configurações.

É o mesmo ajuste em duas configurações → restrinja os filtros de uma (Empresa, TOP, Parceiro, Produto, UF Origem/Destino, Finalidade, Classificação do ICMS, CFOP, Tributação, NCM, Grupos de ICMS, Grupo de Produto, Optante SN, filtro personalizado) até deixar de alcançar o documento, ou mantenha só uma ativa.

Campo Empresa em branco vale para todas.

**(3)** **Precisa ver os ajustes já gravados? Gere em duas etapas.**

- 1ª execução: **Gerar Ajustes = "Não gerar"** → o livro é gerado e permanece.
- 2ª execução: desmarque Gerar Notas, Gerar Financeiro e Gerar Redução Z, com **Gerar Ajustes = "Gerar e atualizar" e deixe marcado Gerar Canceladas**. Se a mensagem voltar, o livro **não** é removido, porque nenhuma dessas ações estava marcada.
- Com o livro preservado, consulte no Cadastro Livro ICMS/IPI a aba Ajustes de Documentos — EFD Fiscal na nota/item indicados.

**(4)**Após as devidas correções nas configurações, gere novamente o livro, usando o processo normal da empresa, se de fato não encontrar mais duplicidades, a mensagem deixa de ser apresentada, e o livro é gerado.

### Causa

A causa deste erro é a configuração duplicada de ajustes de apuração para o mesmo documento fiscal. Isso pode ocorrer quando:

- Duas ou mais configurações de **"Ajustes de Apuração"** possuem critérios de vinculação que se sobrepõem (mesma TOP, mesma natureza de operação, mesmo tipo de documento).
- Houve alteração nas configurações de ajuste sem a devida revisão dos documentos já vinculados anteriormente.

O sistema não permite que o mesmo ajuste seja gerado duas vezes para o mesmo documento, devido aos colaterais nos registros C195/C197, pois isso causaria inconsistência na escrituração fiscal e duplicidade de valores na apuração do ICMS.
