from django.db import models

from django.db import models


# class Pedidos(models.Model):
#     mesa = models.IntegerField(default=0)
#     usuario = models.ForeignKey("Usuario", on_delete=models.SET_NULL, null=True)
#     status = models.BooleanField()
#     hora_pedido = models.TimeField()

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=["id"], name="unique_pedido_id"),
#         ]
#         verbose_name = "Pedido"
#         verbose_name_plural = "Pedidos"

# #  def __str__(self):
# #        return self.nome quais retornar?

# class Usuario(models.Model):
#     cpf = models.CharField(max_length=11, unique=True)
#     tipopessoa = models.ForeignKey("TipoPessoa", on_delete=models.PROTECT)
#     email = models.EmailField(null=True)  # Note: Should be an email field

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=["cpf", "id"], name="unique_usuario_cpf_id"),
#         ]
#         verbose_name = "Usuário"
#         verbose_name_plural = "Usuários"


# class Produtos(models.Model):
#     preco = models.DecimalField(decimal_places=2, max_digits=10)
#     nome = models.CharField(max_length=250)
#     descricao = models.CharField(max_length=255, default="1000")
#     tipoProduto = models.ForeignKey(
#         "TiposProdutos", on_delete=models.SET_NULL, null=True
#     )
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=["id"], name="unique_produto_id"),
#         ]
#         verbose_name = "Produto"
#         verbose_name_plural = "Produtos"

# class TiposProdutos(models.Model):
#     nome = models.CharField(max_length=100)
#     descricao = models.CharField(max_length=1000)

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=["id"], name="unique_tipoproduto_id"),
#         ]
#         verbose_name = "Tipo de Produto"
#         verbose_name_plural = "Tipos de Produtos"


# class ItemPedido(models.Model):
#     pedido = models.ForeignKey("Pedidos", on_delete=models.PROTECT)
#     produto = models.ForeignKey("Produtos", on_delete=models.PROTECT)
#     quantidade = models.IntegerField(default=1)
#     # preco = models.DecimalField(decimal_places=2, max_digits=10) sugestao copilot
#     # total = models.DecimalField(decimal_places=2, max_digits=10) sugestao copilot
#     verbose_name = "Item Pedido"
#     verbose_name_plural = "Itens Pedido"


# class TipoPessoa(models.Model):
#     descricao = models.CharField(max_length=1000)

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=["id"], name="unique_tipopessoa_id"),
#         ]
#         verbose_name = "Tipo de Pessoa"
#         verbose_name_plural = "Tipos de Pessoa"

# #usar protect ou cascade?

# refazendo o modelo ------------->


class TipoPessoa(models.Model):
    descricao = models.CharField(max_length=1000)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Tipo de Pessoa"
        verbose_name_plural = "Tipos de Pessoa"


class Usuario(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    tipopessoa = models.ForeignKey(TipoPessoa, on_delete=models.PROTECT)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.cpf

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class Pedidos(models.Model):
    mesa = models.IntegerField(default=1)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField()
    hora_pedido = models.TimeField()

    def __str__(self):
        return f"{self.mesa} - {self.usuario_id} - {self.status} - {self.hora_pedido}"

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"


class tipoProduto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=1000)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Produto"
        verbose_name_plural = "Tipos de Produtos"


class Produtos(models.Model):
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    nome = models.CharField(max_length=250)
    descricao = models.CharField(max_length=255, default="1000")
    tipoProduto_id = models.ForeignKey(
        tipoProduto, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"


class itemPedido(models.Model):
    pedido_id = models.ForeignKey(Pedidos, on_delete=models.PROTECT)
    produto_id = models.ForeignKey(Produtos, on_delete=models.PROTECT)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.pedido_id} - {self.produto_id} - {self.quantidade}"

    class Meta:
        verbose_name = "Item Pedido"
        verbose_name_plural = "Itens Pedido"
