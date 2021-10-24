from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
	"""Alow users edit their own profile"""

	def has_object_permission(self, request, view, obj):
		"""Check user is trying to edit their own prodile"""

		if request.method in permissions.SAFE_METHODS:
			return True

		return obj.id == request.user.id



class UpdateOwnStatus(permissions.BasePermission):
	"""Alow users update thier own status"""

	def has_object_permission(self, request, view, obj):
		"""Check user is trying to edir their own status"""

		if request.method == permissions.SAFE_METHODS:
			return True

		return obj.id == request.user.id