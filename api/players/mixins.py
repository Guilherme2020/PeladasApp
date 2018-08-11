from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters

from players.permissions import IsPelada, IsOwnerPelada


class FilteringAndOrderingMixin(object):
    """Default settings for filtering """
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )


class IsPeladaMixin(object):
    permission_classes = (
        IsPelada,
    )


class IsOwnerPeladaMixin(object):
    permission_classes = (
        IsOwnerPelada,

    )
