class EmpresaGastronómica:
	'''Esta clase representa una abstracción de una MicroempresaGatronómica'''

	def __init__(self, nombre, direccion):
		self.nombre = nombre
		self.dirección = direccion
		#self.tel = tel
		pass


class Pasteleria (EmpresaGastronómica):
	'''Esta clase representa una abstracción de una Pasteleria'''

	def __init__(self, pastel=[], cliente=[]):
		self.pastel = pastel
		self.cliente = cliente
		pass

	def vender_pastel(self):
		# returns
		pass


class Pastel:
	'''Esta clase representa una abstracción de un pastel '''

	def __init__(self, tipo):
		self.tipo = tipo
		pass


class PastelGourmet (Pastel):
	'''Esta clase representa una abstracción de un pastel gourmet'''

	def __init__(self, cantidad_gourmet, precio_gourmet, sabor_gourmet):
		self.cantidad_gourmet = cantidad_gourmet
		self.precio_gourmet = precio_gourmet
		self.sabor_gourmet = sabor_gourmet
		pass


class PastelEconomico (Pastel):
	'''Esta clase representa una abstracción de un pastel economico'''

	def __init__(self, tamanho_economico, cantidad_economico):
		self.tamanho_economico = tamanho_economico
		self.cantidad_economico = cantidad_economico
		pass


class PastelPequeño (PastelEconomico):
	'''Esta clase representa una abstracción de un pastel pequeño'''

	def __init__(self, sabor_pequenho, precio_pequenho):
		self.sabor_pequenho = sabor_pequenho
		self.precio_pequenho = precio_pequenho
		pass


class PastelMediano (PastelEconomico):
	'''Esta clase representa una abstracción de un pastel mediano'''

	def __init__(self, sabor_mediano, precio_mediano):
		self.sabor_mediano = sabor_mediano
		self.precio_mediano = precio_mediano
		pass


class PastelHelado (Pastel):
	def __init__(self, cantidad_helado, precio_helado, sabor_helado):
		self.cantidad_helado = cantidad_helado
		self.precio_helado = precio_helado
		self.sabor_helado = sabor_helado
		pass


class Menú:
	def __init__(self):
		pass

	def iniciar_sistema(self):
		# returns
		pass

	def recibir_datos(self):
		# returns
		pass


class SistemaFacturación:
	'''Esta clase representa una abstracción de un sistema de facturacion'''

	def __init__(self):
		pass

	def calcular_precio(self):
		# returns
		pass

	def emitir_factura(self):
		# returns
		pass


class Factura:
	def __init__(self, numero, cliente):
		self.numero = numero
		self.cliente = cliente
		pass


class Cliente:
	'''Esta clase representa una abstracción de datos del cliente'''

	def __init__(self, cedula, nombre, direccion):
		self.cedula = cedula
		self.nombre = nombre
		self.direccion = direccion
		pass


class SistemaFacturación:
	'''Esta clase representa una abstracción de un sistema de facturacion'''

	def __init__(self):
		pass

	def calcular_precio(self):
		# returns
		pass

	def emitir_factura(self):
		# returns
		pass


class Cliente:
	'''Esta clase representa una abstracción de datos del cliente'''

	def __init__(self, cedula, nombre, direccion):
		self.cedula = cedula
		self.nombre = nombre
		self.direccion = direccion
		pass
