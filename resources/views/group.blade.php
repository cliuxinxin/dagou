@extends('layouts.app')

@section('content')
    <div class="container">
        <row>
            <h1>报名表</h1>
            <blockquote>
                在这里可以发起报名表，然后把报名表发给大家报名。
            </blockquote>
        </row>
        <hr>
        <div class="row">
            <table class="table table-striped">
                <tr>
                    <th>名称</th>
                    <th>说明</th>
                    <th>网址</th>
                    <th>参加</th>
                </tr>
                @foreach($items as $item)
                    <tr>
                        <td>{{$item->name}}</td>
                        <td>{{str_limit($item->detail, $limit = 100, $end = '...') }}</td>
                        <td><a href="{{$item->url}}">{{$item->url}}</a></td>
                        <td><a class="btn btn-primary" href="{{ route('groupDetail',$item->id) }}">参与</a></td>
                    </tr>
                @endforeach
            </table>
        </div>
        {{ $items->links() }}
        <hr>
        <div class="row col-md-6">
            <form method="POST" action="{{ route('groupStore') }}">
                {{ csrf_field() }}
                <div class="form-group">
                    <label for="name">名称</label>
                    <input type="text" class="form-control" name="name">
                </div>

                <div class="form-group" >
                    <label for="detail">介绍</label>
                    <textarea rows="3" class="form-control" name="detail"></textarea>
                </div>

                <div class="form-group">
                    <label for="url">网址</label>
                    <input type="text" class="form-control" name="url">
                </div>

                <button type="submit" class="btn btn-default">创建</button>
            </form>
        </div>
    </div>
@endsection
