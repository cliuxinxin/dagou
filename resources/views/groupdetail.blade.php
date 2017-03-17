@extends('layouts.app')

@section('content')
    <div class="container">
        <row>
            <h1>{{ $group->name }}</h1>
            <blockquote>
                {{ $group->detail }}
            </blockquote>
            @if($group->url)
                <a href="{{$group->url}}">{{$group->url}}</a>
                @endif
        </row>
        <hr>
        <div class="row">
            <table class="table table-striped">
                <tr>
                    <th>姓名</th>
                    <th>电话</th>
                    <th>备注</th>
                    <th>地址</th>
                </tr>
                @foreach($items as $item)
                    <tr>
                        <td>{{$item->name}}</td>
                        <td>{{$item->phone }}</td>
                        <td>{{$item->detail}}</td>
                        <td>{{$item->address}}</td>
                    </tr>
                @endforeach
            </table>
        </div>
        {{ $items->links() }}
        <hr>
        <div class="row col-md-6">
            <form method="POST" action="{{ route('groupDetailStore',Request::segment(2)) }}">
                {{ csrf_field() }}
                <div class="form-group">
                    <label for="name">姓名</label>
                    <input type="text" class="form-control" name="name">
                </div>

                <div class="form-group">
                    <label for="phone">电话</label>
                    <input type="text" class="form-control" name="phone">
                </div>

                <div class="form-group" >
                    <label for="detail">备注</label>
                    <textarea rows="3" class="form-control" name="detail"></textarea>
                </div>

                <div class="form-group" >
                    <label for="address">地址</label>
                    <input type="text" class="form-control" name="address">
                </div>

                <button type="submit" class="btn btn-success">参加</button>
            </form>
        </div>
    </div>
@endsection
