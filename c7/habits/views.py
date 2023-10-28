from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    """Просмотр всех привычек """

    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class PublicHabitListAPIView(generics.ListAPIView):
    """Просмотр всех публичных привычек """

    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticatedOrReadOnly]


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр одной привычки """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Редактирование привычки """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        updated_habit = serializer.save()
        updated_habit.owner = self.request.user
        updated_habit.save()


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки """

    queryset = Habit.objects.all()
    permission_classes = [IsOwner]