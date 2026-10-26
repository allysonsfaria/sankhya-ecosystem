---
id: "37314330398359"
titulo: "Descrição incorreta dos locais nas Centrais de Vendas e Compras"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37314330398359-Descri%C3%A7%C3%A3o-incorreta-dos-locais-nas-Centrais-de-Vendas-e-Compras"
trilha: "Melhores Práticas > Compras e Estoque"
atualizado_em: "2026-07-22T14:13:27Z"
rotulos: ["Configuração", "Central de Vendas", "DESCRLOCAL", "Preferências", "Parâmetro", "Descrição para Local", "Descrição incorreta dos locais", "Centrais de Vendas e Compas", "Local origem", "Nomenclatura"]
---

# Descrição incorreta dos locais nas Centrais de Vendas e Compras

Ao acessar a Central de Vendas, o campo ''**Local origem''** pode ser exibido com uma descrição diferente do nome padrão.

Esse comportamento ocorre quando o parâmetro **''DESCRLOCAL – Descrição para Local''** está configurado com um valor personalizado.

Nessa situação, o sistema utiliza a descrição informada no parâmetro para renomear o campo ''Local origem'' nas centrais.
 
**Procedimento**

**(1)** Acesse a tela [**''Preferências''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

**(1)** Pesquise pelo parâmetro ''DESCRLOCAL - Descrição para Local''.

**(1)** No campo ''Texto'', insira a descrição desejada.

- Exemplo: “Depósito” ou “Ponto de Expedição”.

**(1)** Salve as alterações.

**(1)** Feche a abra novamente a tela [**''Central de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas) para que a modificação seja aplicada.

Após realizar as configurações, o campo ''Local origem'' exibirá o texto definido no parâmetro **''DESCRLOCAL''**

 
 **OBSERVAÇÃO:** Essa configuração altera apenas a nomenclatura exibida nas Centrais de Vendas e Compras, sem modificar a lógica de funcionamento ou o vínculo do local de origem com o movimento.

Se o nome personalizado não for exibido, verifique se o parâmetro foi salvo corretamente e se não há cache ativo no sistema.
