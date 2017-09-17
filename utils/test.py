# -*- coding: utf-8 -*-
# author: itimor


class SaltCmdrunViewSet(viewsets.ModelViewSet):
    queryset = SaltCmdrun.objects.all()
    serializer_class = SaltCmdrunSerializer

    def create(self, validated_data):
        instance = SaltCmdrun.objects.create(**validated_data)
        return instance

        cmd = self.request.data['cmd']
        results = run(cmd)
        print(results)
        serializer = SaltCmdrunSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(results, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)