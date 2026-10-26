---
id: "360045116193"
titulo: "Substituto por Empresa - Conta Contábil"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116193-Substituto-por-Empresa-Conta-Cont%C3%A1bil"
trilha: "Manual do Produto > Fiscal e Contábil > Contábil > Contabilização"
atualizado_em: "2026-07-29T16:01:31Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Empresa", "Contas", "Substituto por Empresa - Conta Contábil", "br.com.sankhya.substituto.por.empresa.cc", "Substituto por Empresa - Conta Contábil manual", "TOP", "Contabilização", "Cadastro de Conta Contábil Substituta por Empresa"]
---

# Substituto por Empresa - Conta Contábil

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42314960990359) Módulo: Contabilização> Arquivos
```

---

Nessa tela você irá realizar o cadastro de uma conta contábil substituta para uma determinada empresa.

![Imagem 2: Nessa tela você irá realizar o cadastro de uma conta contábil substituta para uma determinada empresa.](https://ajuda.sankhya.com.br/hc/article_attachments/5165315966103)

**Importante:** Essa funcionalidade será aplicada apenas se a conta for variável. Se a TOP de Contabilização estiver marcada como conta constante, a substituição não ocorrerá.

Assim, teremos um exemplo prático:

- É necessário que na [TOP de Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174) o campo **"Tipo de Conta Contábil"** esteja configurado com a opção **"Variável"**.
- Configure esta rotina da seguinte forma:

**Cód. Empresa:** Empresa utilizada para lançamento da contabilização.

**Cód. Origem:** Conta original do lançamento calculada pelo sistema, que será substituída pela conta de destino.

**Cód. Destino:** Conta que irá substituir a conta original utilizada no lançamento contábil.

Quando você cadastrar uma conta substituta para uma determinada empresa e na rotina de contabilização o sistema acabar de resolver a conta contábil que será utilizada para determinado lançamento, ele irá verificar se para aquela empresa e conta existe alguma outra conta para substituí-la e irá utilizá-la.

Lembrando que não basta apenas existir a configuração dessa rotina, se o tipo de conta contábil não for Variável a substituição não irá ocorrer. Existindo a configuração de forma correta, quando a contabilização for solicitada na tela de Agendamento, o sistema irá realizar a substituição.

**Nota:**Se forem cadastradas mais de uma conta destino para uma mesma empresa e uma mesma conta origem e a conta for variável, o sistema aceitará o cadastro, mas fará a substituição referente ao primeiro registro cadastrado na tela.
