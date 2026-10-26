---
id: "44120480928023"
titulo: "Solução não listada nas Configurações Gateway"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44120480928023-Solu%C3%A7%C3%A3o-n%C3%A3o-listada-nas-Configura%C3%A7%C3%B5es-Gateway"
trilha: "Manual do Produto > Plataforma e Integrações > Plataforma"
atualizado_em: "2026-10-14T17:07:12Z"
rotulos: ["API Gateway"]
---

# Solução não listada nas Configurações Gateway

**SITUAÇÃO**

Apos criar uma solução de uso próprio no [Portal do Desenvolvedor](https://areadev.sankhya.com.br), a aplicação não é listada ao realizar a busca na tela de Configurações Gateway (caminho: Configurações >> Avançado) no Sankhya Om. Como consequência, não é possível gerar o token de integração (X-Token).

**SOLUÇÃO**

Para localizar a sua aplicação corretamente, siga os passos abaixo:

**(1)** Acesse o **Portal do Desenvolvedor** (Área Dev) e navegue até a aba **Minhas Soluções**.

**(2)** Abra ou clique em editar a solução que você criou e que não está aparecendo.

**(3)** Procure pelo campo **"Título do componente"** e verifique exatamente o nome que está preenchido nele (por         exemplo, "Meu Componente").

![Imagem 1: (3) Procure pelo campo "Título do componente" e verifique exatamente o nome que está preenchido nele (por exemplo, "Meu…](https://ajuda.sankhya.com.br/hc/article_attachments/44120480921879)

**(4)** Retorne ao Sankhya Om e acesse a tela **Configurações Gateway**.

Ao realizar a busca da aplicação, pesquise utilizando **exatamente o nome encontrado no "Título do componente"** ou busque pelo **nome da sua organização**.

![Imagem 2: Ao realizar a busca da aplicação, pesquise utilizando exatamente o nome encontrado no "Título do componente" ou busque…](https://ajuda.sankhya.com.br/hc/article_attachments/44120452185111)

**⚠️ Importante:** Se você pesquisar pelo nome do componente, o sistema não retornará resultados. A busca exige o Titulo do Componente ou nome da sua organização.

![Imagem 3: ⚠️ Importante: Se você pesquisar pelo nome do componente, o sistema não retornará resultados. A busca exige o Titulo do…](https://ajuda.sankhya.com.br/hc/article_attachments/44120452185751)

**Causa**

Isso ocorre porque o sistema realiza a busca na tela de Configurações do Gateway com base no **"Título do Componente"** definido na solução (no processo de criação na areadev.sankhya.com.br) ou pelo nome da sua Organização, e não pelo nome do Componente.

**Ainda não conseguiu encontrar sua solução?**
Se após pesquisar pelo Título do componente exato a aplicação continuar não aparecendo, o comportamento pode estar relacionado à falta de vínculo do usuário criador da solução com a organização/base.
